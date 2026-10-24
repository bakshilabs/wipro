import { chromium } from 'playwright';
const p=process.argv[2]||'overview';
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const c=await b.newContext({viewport:{width:1280,height:720}});
await c.addInitScript(()=>{try{sessionStorage.setItem('pw','ok')}catch(e){}});
const pg=await c.newPage();const errs=[];pg.on('pageerror',e=>errs.push(e.message));
await pg.goto('file:///home/user/wipro/'+p+'.html');await pg.waitForTimeout(800);
const st=()=>pg.evaluate(()=>[scrollY,document.querySelector('.st-n').textContent]);
const log=[];
await pg.mouse.move(640,400);
for(let i=0;i<3;i++){for(let k=0;k<8;k++){await pg.mouse.wheel(0,40);await pg.waitForTimeout(15)}await pg.waitForTimeout(1100);log.push(['wheel',...await st()])}
await pg.mouse.wheel(0,-120);await pg.waitForTimeout(1100);log.push(['wheelup',...await st()]);
await pg.keyboard.press('ArrowDown');await pg.waitForTimeout(1100);log.push(['arrow',...await st()]);
await pg.keyboard.press('PageDown');await pg.waitForTimeout(1100);log.push(['pgdn',...await st()]);
const labels=await pg.evaluate(()=>[...document.querySelectorAll('.dots button')].map(b=>b.getAttribute('aria-label')));
await pg.hover('.dots li:nth-child(2) button');await pg.click('.dots li:nth-child(2) button');await pg.waitForTimeout(1100);log.push(['dot2',...await st()]);
await pg.screenshot({path:`dk_${p}.png`});
await pg.click('.st-mode');await pg.mouse.wheel(0,200);await pg.waitForTimeout(500);log.push(['free',...await st()]);
console.log(JSON.stringify(log));console.log(labels.join(' | '));console.log(errs);await b.close();
