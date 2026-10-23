import { chromium } from 'playwright';
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const c=await b.newContext({viewport:{width:390,height:900},reducedMotion:'reduce'});
await c.addInitScript(()=>{try{sessionStorage.setItem('pw','ok')}catch(e){}});
const pg=await c.newPage();await pg.goto('file:///home/user/wipro/role.html');
console.log(await pg.evaluate(()=>{const r=document.querySelector('.rail');const t=r.querySelector('.tile');const p=t.querySelector('p:last-child');return [r.clientWidth,r.scrollWidth,t.getBoundingClientRect().width,p.getBoundingClientRect().width,getComputedStyle(r).gridAutoColumns,getComputedStyle(p).whiteSpace]}));
await b.close();
