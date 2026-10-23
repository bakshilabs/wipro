"""Builds every page of the site into the repository root. Run: python3 build/build.py"""
import hashlib, importlib, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib

# The password is not stored in the repository; only its salted SHA-256 hash is.
PASSWORD_HASH = "90c12ce398a4ae8d8199011ddb1afa0a79e444deffa5817446f933ef21a17a32"


def gate():
    ok = ",".join(f'"{f}"' for f in lib.GUARD_PAGES)
    doc = lib.head("Enter Password", "Password page for the Wipro DX application site.", guard=False) + f"""
<body>
<style>
.gate{{min-height:100vh;display:grid;place-items:center;padding:24px}}
.gate form{{width:100%;max-width:420px;background:var(--panel);border-radius:6px;padding:40px 36px}}
.gate h1{{font-size:32px;letter-spacing:-.03em;line-height:1.1}}
.gate p{{color:var(--muted);margin-top:12px;font-size:15px}}
.gate label{{display:block;margin-top:28px;font:500 13px/1 var(--sans);color:var(--muted)}}
.gate input{{width:100%;margin-top:10px;padding:14px 16px;border-radius:4px;border:1px solid var(--line);background:var(--bg);color:var(--ink);font:400 17px/1.2 var(--sans)}}
.gate button{{width:100%;margin-top:16px;padding:14px 16px;border:0;border-radius:3px;background:#4a1fb8;color:#fff;font:500 16px/1 var(--sans);cursor:pointer;min-height:44px}}
.gate button:hover{{filter:brightness(1.15)}}
.gate .err{{min-height:22px;margin-top:12px;color:var(--bad);font-size:14px}}
</style>
<main class="gate" id="main">
<form id="f" autocomplete="off">
<h1>Wipro Digital Experience</h1>
<p>Enter the password you were given to view the role analysis, account map, pursuit model and CV.</p>
<label for="pw">Password</label>
<input id="pw" type="password" autocomplete="current-password" required autofocus>
<button type="submit">View the site</button>
<div class="err" id="err" role="alert" aria-live="polite"></div>
</form>
</main>
<script>
(function(){{
var HASH="{PASSWORD_HASH}",SALT="{lib.SALT}";
var OK=[{ok}];
function hex(b){{return Array.prototype.map.call(new Uint8Array(b),function(x){{return ("0"+x.toString(16)).slice(-2)}}).join("")}}
function dest(){{var n=new URLSearchParams(location.search).get("next");return OK.indexOf(n)>-1?n:"overview.html"}}
try{{if(sessionStorage.getItem("pw")==="ok"){{location.replace(dest());return}}}}catch(e){{}}
document.getElementById("f").addEventListener("submit",function(e){{
 e.preventDefault();var err=document.getElementById("err");err.textContent="";
 if(!window.crypto||!crypto.subtle){{err.textContent="This browser cannot check the password on an insecure connection.";return}}
 crypto.subtle.digest("SHA-256",new TextEncoder().encode(SALT+document.getElementById("pw").value.trim())).then(function(h){{
  if(hex(h)===HASH){{try{{sessionStorage.setItem("pw","ok")}}catch(x){{}}location.replace(dest())}}
  else{{err.textContent="That password is not correct.";document.getElementById("pw").select()}}
 }});
}});
}})();
</script>
</body>
</html>
"""
    with open(os.path.join(lib.ROOT, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(doc)
    print("wrote index.html")


if __name__ == "__main__":
    gate()
    only = sys.argv[1:]
    for f, _, _ in lib.PAGES:
        mod = "p_" + f[:-5].replace("-", "_")
        if only and mod not in only and f not in only:
            continue
        if os.path.exists(os.path.join(os.path.dirname(__file__), "pages", mod + ".py")):
            m = importlib.import_module("pages." + mod)
            m.build()
