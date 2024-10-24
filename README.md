# acupter
cordova to build acupuncture assistant

### Live Demo

[https://dna2github.github.io/acupter/](https://dna2github.github.io/acupter/)

![Demo: Acupter](https://dna2github.github.io/acupter/screenshot/acupter-demo-1.jpg "Acupter")

### Build

```
npm install
# build electron native op native.js
webpack

# build electron UI into www
cd src
npm install
npm run build
# after this build, the www folder can be deployed directly as a standalone website

# ensure in electron, classic level db can work
cp -r node_modules/classic-level/prebuilds platforms/electron/platform_www/prebuilds

# test in electron
cordova run electron
# test in web browser
cd src && npm run dev
```
