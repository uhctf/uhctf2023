// Code to render pages

import { logged_in } from "./auth.js";

function add_index(app) {
    app.get('/', logged_in, (req, res) => { res.render('index', { username: req.user.username, balance: req.user.balance }) });
}

export { add_index };
