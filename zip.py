import os
import zipfile

base = "spectra-website"

files = {
"website/index.html": """<!DOCTYPE html>
<html>
<head>
<title>Spectra Laboratory</title>
<link rel="stylesheet" href="style.css">
</head>
<body>

<header>
<h2>Spectra Laboratory</h2>
</header>

<section class="hero">
<h1>Advanced Health Checkup</h1>
<a href="https://wa.me/919327650991">WhatsApp Now</a>
</section>

</body>
</html>
""",

"website/style.css": """body {
font-family: Arial;
margin: 0;
}
header {
background:#0A4D8C;
color:white;
padding:15px;
}
.hero {
padding:50px;
background:#3AA6FF;
color:white;
text-align:center;
}
""",

"server/server.js": """const express=require('express');
const mongoose=require('mongoose');
const cors=require('cors');

const app=express();
app.use(express.json());
app.use(cors());

mongoose.connect("mongodb://127.0.0.1:27017/spectra");

const Package=mongoose.model("Package",{name:String});

app.get("/",(req,res)=>res.send("Server Running"));

app.listen(5000,()=>console.log("Running"));
"""
}

for path, content in files.items():
    full_path = os.path.join(base, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

zip_name = "spectra-website.zip"
with zipfile.ZipFile(zip_name, 'w') as z:
    for root, dirs, files in os.walk(base):
        for file in files:
            filepath = os.path.join(root, file)
            z.write(filepath)

print("ZIP Created:", zip_name)