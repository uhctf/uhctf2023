// All authentication code

import session from 'express-session';
import passport from 'passport';
import passport_local from 'passport-local';
import bodyParser from 'body-parser';


// Our 'database'
const USERS = new Map();
USERS.set('demo', { password: "password", balance: 0.05 });

// Authentication using a well-established framework
const user_fields = {
    username: "username", password: "password"
};
const auth_callback = (username, password, done) => {
    const user = USERS.get(username);
    if (!user)
        return done(null, false, { message: "user doesn't exist" });
    if (user.password !== password)
        return done(null, false, { message: 'could not sign in with those credentials' });

    return done(null, { username: user.username, balance: 0.05 });
};
passport.use('local', new passport_local.Strategy(user_fields, auth_callback));

// Put the user in the session
passport.serializeUser(function (user, done) {
    done(null, JSON.stringify(user));
});
passport.deserializeUser(function (user, done) {
    done(null, JSON.parse(user));
});

// Passport code
const post_login = passport.authenticate('local', {
    successRedirect: "/",
    failureRedirect: "/login"
});
const get_login = (req, res) => {
    res.render('login');
};

// Middleware to make sure that you're logged in before allowing a route
const logged_in = (req, res, next) => {
    if (req.user) {
        next();
    } else {
        res.redirect("/login");
    }
}

const not_logged_in = (req, res, next) => {
    if (req.user === undefined) next();
    else res.redirect("/");
}

const post_logout = (req, res) => {
    req.user = undefined;
    res.redirect("/login");
}

function add_authentication(app) {
    // use express-session for session management
    app.use(session({
        secret: process.env["SECRET"] || "dummysecret",
        resave: false,
        saveUninitialized: false
    }));

    // Add parsing to the body, so that we can read username and password
    app.use(bodyParser.json());
    app.use(bodyParser.urlencoded({ extended: true }));

    // Initialize passport
    app.use(passport.authenticate('session'));

    app.post('/login', post_login);
    app.get('/login', get_login);

    app.post('/logout', post_logout);
}

export { add_authentication, logged_in };