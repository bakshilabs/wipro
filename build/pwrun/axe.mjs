import { chromium } from 'playwright';
import fs from 'fs';
const axe=fs.readFileSync('node_modules/axe-core/axe.min.js','utf8');
const pages=['index','overview','role','operating-model','market','triggers','accounts','pursuit','portfolio','plan','fit','cv'];
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const sch of ['light','dark']){const c=await b.newContext({colorScheme:sch,viewport:{width:1280,height:900}});
 await c.addInitScript(()=>{try{if(!location.pathname.endsWith('index.html'))sessionStorage.setItem('pw','ok')}catch(e){}});
 for(const p of pages){const pg=await c.newPage();await pg.goto('file:///home/user/wipro/'+p+'.html');await pg.waitForTimeout(300);
  await pg.addScriptTag({content:axe});const r=await pg.evaluate(async()=>await axe.run(document,{runOnly:['wcag2a','wcag2aa','best-practice']}));
  for(const v of r.violations)console.log(sch,p,v.id,v.impact,v.nodes.length,v.nodes.slice(0,2).map(n=>n.target.join(' ')+' :: '+(n.failureSummary||'').slice(0,160)).join(' | '));
  await pg.close();}
 await c.close();}
await b.close();
