/**
* @ CC3688
* email:442677028@qq.com
*/
'use strict';
 
let fs = require("fs");

fs.readFile('./readme.txt','utf-8',function(err,data){
    if(err){
        console.log(err);
    }else{
        console.log(data);   
    }
});

fs.readFile('./timg.jpeg',function(err,data){
    if(err){
        console.log(err);
    }else{
        console.log(data);
        console.log(data.length+'btytes');
    }
});

fs.stat('./timg.jpeg',function(err,stat){
    if(err){
        console.log(err);
    }else{
        console.log('isFile: '+ stat.isFile());
        console.log('size: '+ stat.size);
        console.log('birth time: '+ stat.birthtime);
    }
});