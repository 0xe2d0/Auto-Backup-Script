# ABS-Project
<img src="https://user-images.githubusercontent.com/85255852/130467971-39c23f87-2ef7-4db4-a779-ea0d18e9f9ff.png"/>

## 🌴 Description 
**ABS Project** is a minimal backup service. When run the **abs.py** file , backs up files and folders in that directory to the **backup/** directory.


## ⚒️ Installation
<pre><code>git clone https://github.com/coderpyxd/ABS-Project</code></pre>
<pre><code>cd ABS-Project</code></pre>
<pre><code>chmod 777 abs.py</code></pre>
<pre><code>pip3 install -r requirements.txt</code></pre>
**That's it 🤠**

## 🛡️ Usage
<strong> Now that you have completed the installation, copy the *abs.py* file into the folder you want backup.</strong>

Help Command :
    <pre><code>python3 abs.py -h</code></pre> 
    
Other Parameters Description:
    <ul>
       <li>**-p --path** : Path of the folder to be backed up. Default : **your path**</li>
       <li>**-o --output** : Folder path of backups . Default: **../backup/**</li>
       <li>**-l --log-file** : Name of log file. Default :** backup.log**</li>
       <li>**-t --time**: Time range of backups. Default:** 20 second** </li>
    </ul>
    
**The default use of parameters is sufficient for you, but if you want to change them, you can read these explanations.**

## That's it , after running this, your project will be backed up in the timeframes you set.
