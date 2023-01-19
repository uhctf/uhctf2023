import express from 'express';
// Code to serve static files

function add_static_files(app) {
    app.use(express.static('static'));
}

export { add_static_files };
