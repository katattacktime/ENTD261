var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function (req, res) {
    res.render('ethics.html', { title: 'OGT Ethics' });
});

module.exports = router;