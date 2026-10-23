import { chromium } from 'playwright';
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const c=await b.newContext({colorScheme:'light'});
await c.addInitScript(()=>{try{sessionStorage.setItem('pw','ok')}catch(e){}});
const pg=await c.newPage();await pg.goto('file:///home/user/wipro/cv.html');await pg.emulateMedia({media:'print'});await pg.waitForTimeout(400);
await pg.pdf({path:'/home/user/wipro/arpan-bakshi-cv-wipro.pdf',format:'A4',printBackground:true,preferCSSPageSize:true});await b.close();
