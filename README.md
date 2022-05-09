# Ward/Stake activity rate approximation

This script, from https://reasoningmywaythroughmyfaith.blogspot.com/2020/04/find-out-how-many-members-of-your-steak.html, pulls the number of members in your stake who have callings, broken down per ward. This gives you a rough approximation of the adult activity rate of your local units.

## How to use

1. Log in to https://directory.churchofjesuschrist.org/
1. Open developer tools
1. Switch the unit dropdown in the top left to "Entire Stake"
1. Filter the Network tab by "households"
1. Open one of the requests and grab the `authorization` bearer token from the request headers
1. Paste that into `bearer=''`
1. Grab the unit with this command in the console: `window.location.href.substring(window.location.href.lastIndexOf('/')+1)`
1. Grab the `directoryAccessToken` with this command: `document.cookie.match(new RegExp('(^| )directory_access_token=([^;]+)'))[2]`
1. Grab the `directoryIdentityToken` with this command: `document.cookie.match(new RegExp('(^| )directory_identity_token=([^;]+)'))[2]`
1. Save that all and run the script

