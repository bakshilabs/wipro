import { chromium } from 'playwright';
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const c=await b.newContext({colorScheme:'light',viewport:{width:1280,height:900}});
await c.addInitScript(()=>{try{sessionStorage.setItem('pw','ok')}catch(e){}});
for(const [p,y] of [['overview',0],['market-outlook',0],['market-outlook',1400],['services-comparison',0],['conferences',0]]){const pg=await c.newPage();await pg.goto('file:///home/user/populous/'+p+'.html');await pg.waitForTimeout(1500);await pg.evaluate(y=>scrollTo(0,y),y);await pg.waitForTimeout(400);await pg.screenshot({path:`pop_${p}_${y}.png`});await pg.close()}
await b.close();
