['C:\\nodejs\\node.exe', 'C:\\ENTD261\\w4_args.js']
console.log(process.argv);

if (process.argv.length <= 2) {

    console.log("Usage: " + " SOME_PARAM");

    process.exit(-1);

}

console.log('Params: ' + process.argv.length);

console.log('University: ' + process.argv[2]);

console.log('Class: ' + process.argv[3]);

// Test the code
// node w4_args.js
// node w4_args.js Apus ENTD261 