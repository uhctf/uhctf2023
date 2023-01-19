import express from 'express';

import { add_authentication, logged_in } from './auth.js';
import { add_tip } from './tip.js';
import { add_index } from './index.js';
import { add_static_files } from './static.js';

// create the Express app
const app = express();
app.set('view engine', 'pug');

// Add the different modules
add_authentication(app);
add_tip(app);
add_index(app);
add_static_files(app);

// Check if a flag is set
if (!process.env.FLAG) {
    console.log("No FLAG is set")
}

// start the server
const port = Number(process.env.PORT) || 3000;
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});
