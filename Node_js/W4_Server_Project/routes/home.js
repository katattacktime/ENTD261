var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function (req, res) {
    res.render('home.html', { title: 'Orange Groves Tea' });
});

module.exports = router;