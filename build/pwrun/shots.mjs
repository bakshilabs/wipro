import { chromium } from 'playwright';
const pages=(process.argv[2]||'role,operating-model,market,triggers,accounts,pursuit,portfolio').split(',');
const full=process.argv[3]==='full';
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const sch of (process.argv[4]||'light').split(',')) for(const [w,tag] of [[1280,'d'],[390,'m']]){
 const c=await b.newContext({colorScheme:sch,viewport:{width:w,height:900}});
 await c.addInitScript(()=>{try{sessionStorage.setItem('pw','ok')}catch(e){}});
 for(const p of pages){const pg=await c.newPage();const errs=[];pg.on('pageerror',e=>errs.push(e.message));
  await pg.goto('file:///home/user/wipro/'+p+'.html');await pg.waitForTimeout(400);
  const o=await pg.evaluate(()=>document.documentElement.scrollWidth-innerWidth);
  if(o>0)console.log('HSCROLL',sch,w,p,o); if(errs.length)console.log('ERR',p,errs);
  if(full&&tag==='d') await pg.screenshot({path:`s_${p}_${sch}.png`,fullPage:true});
  await pg.close();}
 await c.close();}
await b.close();
