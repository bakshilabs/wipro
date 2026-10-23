import { chromium } from 'playwright';
const [p,sch,w,y]=[process.argv[2],process.argv[3]||'light',+(process.argv[4]||1280),+(process.argv[5]||0)];
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const c=await b.newContext({colorScheme:sch,viewport:{width:w,height:900},reducedMotion:'reduce'});
await c.addInitScript(()=>{try{sessionStorage.setItem('pw','ok')}catch(e){}});
const pg=await c.newPage();await pg.goto('file:///home/user/wipro/'+p+'.html');await pg.evaluate(y=>window.scrollTo(0,y),y);await pg.waitForTimeout(300);
await pg.screenshot({path:`t_${p}_${sch}_${w}_${y}.png`});await b.close();
