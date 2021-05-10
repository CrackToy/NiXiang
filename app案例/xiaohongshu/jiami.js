

function showStacks() {
    Java.perform(function() {
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
    });
}


function hook() {
    Java.perform(function () {
        var encryptImei = Java.use("com.xingin.utils.core.ag");
        encryptImei.a.overload('java.lang.String', 'java.lang.String').implementation = function (str,key) {
            console.log("str",str);
            console.log("key",key);
            var ret = this.a(str,key);
            console.log("ret",ret);

            return ret
        };
    })
};

// setImmediate(function () {
//     setTimeout(hook, 0);
// })