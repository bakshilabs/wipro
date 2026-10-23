import { chromium } from 'playwright';
const p=process.argv[2]||'overview';
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const c=await b.newContext({viewport:{width:1280,height:720},reducedMotion:'reduce'});
await c.addInitScript(()=>{try{sessionStorage.setItem('pw','ok')}catch(e){}});
const pg=await c.newPage();const errs=[];pg.on('pageerror',e=>errs.push(e.message));
await pg.goto('file:///home/user/wipro/'+p+'.html');await pg.waitForTimeout(800);
await pg.screenshot({path:`st_${p}_0.png`});
const ys=[];for(let i=0;i<4;i++){await pg.click('.st-down');await pg.waitForTimeout(400);ys.push(await pg.evaluate(()=>[scrollY,document.querySelector('.st-n').textContent]));await pg.screenshot({path:`st_${p}_${i+1}.png`});}
await pg.click('.st-up');await pg.waitForTimeout(400);ys.push(await pg.evaluate(()=>[scrollY,document.querySelector('.st-n').textContent]));
console.log(JSON.stringify(ys),errs);await b.close();
