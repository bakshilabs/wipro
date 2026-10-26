import { chromium } from 'playwright';
const out=process.argv[2];
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const scheme of ['light','dark']){
const c=await b.newContext({viewport:{width:1340,height:770},colorScheme:scheme});
await c.addInitScript(()=>{try{sessionStorage.setItem('pw','ok')}catch(e){}});
const pg=await c.newPage();const errs=[];pg.on('pageerror',e=>errs.push(e.message));
await pg.goto('file:///home/user/wipro/icd-deck.html');await pg.waitForTimeout(300);
for(let n=1;n<=8;n++){
  const ov=await pg.evaluate(()=>{const s=document.querySelector('.slide.on');const r=s.getBoundingClientRect();return [...s.querySelectorAll('*')].filter(e=>{const q=e.getBoundingClientRect();return q.bottom>r.bottom+1||q.right>r.right+1}).map(e=>e.tagName+'.'+e.className).slice(0,5)});
  if(ov.length)console.log(scheme,n,'overflow',ov);
  if(scheme==='light'||n<3)await pg.screenshot({path:`${out}/${scheme}-${n}.png`});
  await pg.keyboard.press('ArrowRight');
}
if(scheme==='light'){await pg.pdf({path:`${out}/deck.pdf`,width:'1280px',height:'720px',printBackground:true});}
console.log(scheme,errs);await c.close();}
await b.close();
