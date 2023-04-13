import { body, validationResult } from "express-validator";
import { logged_in } from "./auth.js";

const get_tip = (req, res) => {
    res.render('tip', { username: req.username, balance: req.balance })
}

const post_tip = (req, res) => {
    const balance = req.user.balance;
    const username = req.user.username;

    // Validate and parse input
    const validation = validationResult(req);
    if (!validation.isEmpty()) {
        return res.render('tip', { username, balance, error: 'Invalid request' });
    }

    const requested_tip = Number(req.body.amount);
    if (!requested_tip) {
        return res.render('tip', { username, balance, error: 'Invalid value' });
    }

    // You cannot tip more than you have
    if (requested_tip > balance) {
        return res.render('tip', { username, balance, error: 'Balance insufficient' });
    }

    // Only allow rounded tips
    const rounded = parseInt(requested_tip);
    if (rounded === 0) {
        return res.render('tip', { username, balance, error: 'Tip cannot be zero.' });
    }

    // All good, register the tip
    // TODO: write this to a db, make sure to lower the balance...

    const flag = process.env.FLAG;
    res.render('tip', { username, balance, flag });
}

function add_tip(app) {
    app.get("/tip", logged_in, get_tip);
    app.post("/tip", logged_in, body('amount').isString(), post_tip);
}

export { add_tip };