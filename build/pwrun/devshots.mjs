import { chromium } from 'playwright';
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
async function shot(page,w,h,sel,out,dpr,sch){const c=await b.newContext({colorScheme:sch,viewport:{width:w,height:h},deviceScaleFactor:dpr,reducedMotion:'reduce'});
 await c.addInitScript(()=>{try{sessionStorage.setItem('pw','ok')}catch(e){}});const pg=await c.newPage();await pg.goto('file:///home/user/wipro/'+page+'.html');await pg.waitForTimeout(800);
 await pg.evaluate(s=>{const e=document.querySelector(s);const y=e.getBoundingClientRect().top+scrollY-70;scrollTo(0,y)},sel);await pg.waitForTimeout(500);
 await pg.screenshot({path:'/home/user/wipro/assets/shots/'+out});await c.close();}
await shot('accounts',1440,900,'.hero-x .art','laptop.png',1,'dark');
await shot('fit',390,845,'.hero-x .art','phone.png',2,'light');
await b.close();
