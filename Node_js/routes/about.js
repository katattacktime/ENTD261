var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function (req, res) {
    res.render('about.html', { title: 'OGT About' });
});

module.exports = router;