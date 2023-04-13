<!doctype html>
<html lang="en">
<head>
    <?php include 'head.php';?>
    <link rel="stylesheet" href="signin.css">
    <title>Sign in example • Pico.css</title>
</head>
<body>
    <nav>
    <?php include 'nav.php';?>
    </nav>

    <!-- Main -->
    <main>
      <article>
        <div>
          <hgroup>
            <h1>Sign in</h1>
          </hgroup>
          <form>
            <input type="text" name="login" placeholder="Login" aria-label="Login" autocomplete="nickname" required>
            <input type="password" name="password" placeholder="Password" aria-label="Password" autocomplete="current-password" required>
            <fieldset>
              <label for="remember">
                <input type="checkbox" role="switch" id="remember" name="remember">
                Remember me
              </label>
            </fieldset>
            <button type="submit" onclick="event.preventDefault()">Login</button>
          </form>
        </div>
        <div></div>
      </article>
    </main><!-- ./ Main -->

    <footer>
    <?php include 'foot.php';?>
    </footer>
  </body>

</html>