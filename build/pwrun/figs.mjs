import { chromium } from 'playwright';
const pages=process.argv[2].split(',');const sch=process.argv[3]||'light';
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const c=await b.newContext({colorScheme:sch,viewport:{width:1280,height:900},reducedMotion:'reduce'});
await c.addInitScript(()=>{try{sessionStorage.setItem('pw','ok')}catch(e){}});
for(const p of pages){const pg=await c.newPage();await pg.goto('file:///home/user/wipro/'+p+'.html');await pg.waitForTimeout(300);
 const els=await pg.$$(process.argv[4]||'figure.fig, .calc');let i=0;for(const e of els){await e.screenshot({path:`f_${p}_${i++}_${sch}.png`});}
 await pg.close();}
await b.close();
