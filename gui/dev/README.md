# Mock API for UI development

A tiny fake backend that serves made-up hosts and filesystems, so you can work
on the GUI without the VPN, the ssh tunnel or the Flask server. It uses only
Node's built-in `http` module, so there is nothing to install.

The data mirrors the real API's JSON shapes and covers every status the UI can
show: in sync, out of sync, no backups, ignored, and backup copy.

## Run it

You need three things running at once, each in its own terminal tab.

1. Tell the front end to skip login (one time only). `.env.local` is gitignored,
   so it will not be committed:

       cd gui
       echo "VITE_AUTH_DISABLED=true" > .env.local

2. Start the mock API (listens on port 5050, the same port `gui/.env` expects):

       cd gui
       node dev/mock-api.mjs

   It prints `mock api on 5050`. Leave this tab alone; a running program
   cannot take other commands, so use a new tab for anything else.

3. Start the front end in another tab:

       cd gui
       npm run dev

4. Open http://localhost:5173 and hard-refresh (Cmd+Shift+R).

Restart `npm run dev` after creating or changing `.env.local`, because Vite only
reads env files at startup.

## Good pages to look at

- `/` : hosts list
- `/hosts/2/filesystems/110` : an out-of-sync filesystem
- `/hosts/4/filesystems/118` : a backup copy (shows the Backup of link)
- Click the `?` button (bottom right) for the status legend.

## Stop it

Press Ctrl+C in the tab running the mock API. If something else is holding
port 5050, `lsof -i :5050` shows the process ID, and `kill <that number>`
stops it.

## Caveats

- The data is fake. This only shows how the UI looks and behaves; it does not
  test the real API or real backup states.
- Remove `.env.local` (or set `VITE_AUTH_DISABLED=false`) when you want to test
  against the real, authenticated backend.
