import { chromium } from 'playwright';
const [p,sch,w]=[process.argv[2],process.argv[3]||'light',+(process.argv[4]||1280)];
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const c=await b.newContext({colorScheme:sch,viewport:{width:w,height:900},reducedMotion:'reduce'});
await c.addInitScript(()=>{try{sessionStorage.setItem('pw','ok')}catch(e){}});
const pg=await c.newPage();await pg.goto('file:///home/user/wipro/'+p+'.html');await pg.waitForTimeout(1200);
const h=await pg.evaluate(()=>document.documentElement.scrollHeight);
for(let y=0,i=0;y<h;y+=1800,i++){await pg.screenshot({path:`v_${p}_${sch}_${w}_${i}.png`,clip:{x:0,y,width:w,height:Math.min(1800,h-y)},fullPage:true});}
console.log(p,h);await b.close();
