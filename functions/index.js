const {initializeApp}=require('firebase-admin/app');
const {getFirestore,FieldValue}=require('firebase-admin/firestore');
const {onDocumentCreated}=require('firebase-functions/v2/firestore');
const {createHash}=require('node:crypto');
initializeApp();
const db=getFirestore();
const root='apps/playprint';
async function credit(kind,uid,identity,source,time){
  if(typeof uid!=='string'||!uid||uid.includes('/'))return;
  const id=createHash('sha256').update(JSON.stringify([kind,uid,identity])).digest('hex');
  const ref=db.doc(root+'/achievementLedger/'+id);
  await db.runTransaction(async tx=>{
    if((await tx.get(ref)).exists)return;
    tx.create(ref,{kind,uid,source,occurredAt:time,recordedAt:FieldValue.serverTimestamp()});
  });
}
exports.recordPost=onDocumentCreated(root+'/activity/{postId}',async e=>{
  const p=e.data?.data();if(!p)return;
  await credit('post',p.authorId,e.params.postId,e.data.ref.path,e.data.createTime);
  if(p.type==='review'&&typeof p.gameId==='string'&&p.gameId)
    await credit('reviewedGame',p.authorId,p.gameId,e.data.ref.path,e.data.createTime);
});
exports.recordReaction=onDocumentCreated(root+'/activity/{postId}/reactions/{uid}',async e=>{
  if(!e.data)return;
  const {postId,uid}=e.params;
  await credit('reactedPost',uid,postId,e.data.ref.path,e.data.createTime);
  const post=await db.doc(root+'/activity/'+postId).get();
  const author=post.data()?.authorId;
  if(author&&author!==uid)await credit('receivedReaction',author,[postId,uid],e.data.ref.path,e.data.createTime);
});
exports.recordFollow=onDocumentCreated(root+'/follows/{edgeId}',async e=>{
  const p=e.data?.data();if(p&&p.from!==p.to&&typeof p.to==='string')
    await credit('followedAccount',p.from,p.to,e.data.ref.path,e.data.createTime);
});
// Comments and speed awards require additional abuse controls and timestamp validation.
// Backfill must use retained source records and the same identity keys.
