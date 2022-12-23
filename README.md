# Ward/Stake activity rate approximation

This script, (modified slightly from the [original script here](https://reasoningmywaythroughmyfaith.blogspot.com/2020/04/find-out-how-many-members-of-your-steak.html)), calculates one measure of what percentage of Mormons in your area are "active".

It pulls the number of adult members in your stake who have callings, broken down per ward/branch. This gives you a rough approximation of the adult activity rate of your local units.

**NOTE:** You must have a valid "Church Account" for this to work. If you've been excommunicated or have resigned, this won't work for you.

## How to use

1. Log in to https://directory.churchofjesuschrist.org/
1. Open developer tools in your browser (Ctrl+Shift+J or Cmd+Option+J usually works)
1. Switch the unit dropdown in the top left to "Entire Stake"
1. Grab the `unit` from the end of the URL, or by running this command in the console:
    * `window.location.href.substring(window.location.href.lastIndexOf('/')+1)`
    * This will be a number around 6 or 7 digits long
1. Grab the `appSession` cookie from one of the valid requests executed by the page:
   1. Open the Network tab
   1. Find a request for `households?unit=`
   1. Go to the Headers tab of that request
   1. Scroll down to Request Headers
   1. Find the Cookie header
   1. Within that cookie, usually at the end, find the value of `appSession`. This will be a really long alphanumeric string.
1. Paste those values into the corresponding variables at the top of the file
1. Save that all and run the script with `python3 stats.py`

You can save your unit number, because it won't change unless your stake gets reorganized. But you'll need to grab a new session cookie when you run the script again in the future.

## Sample output

```
stake: Somewhere USA Stake
childUnit: Anytown Ward
Adult members in ward: 609
Adult members with callings: 136
Adult members without a calling: 473
Adult members with multiple callings: 19
Adult members in the ward with Stake callings: 22
Average estimated adult activity in ward: 0.2233169129720854

...
<continues with the other units in the stake>
...

Adult members in Stake: 3681
Adult members in Stake with callings: 1060
Average estimated adult activity in stake: 0.28796522684053244
```

This tells you there is a 22% activity rate in the Anytown Ward, and a 29% activity rate across the entire Somewhere USA Stake.

## Troubleshooting

### ModuleNotFoundError: No module named 'requests'

`sudo pip3 install requests`

### json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

This is probably because your credentials are out of date. Fetch the `appSession` cookie again and retry.

## Future work

* Default to JSON output, to make the results easier to import into a spreadsheet or to query on the command line with `jq`
* Make an easier way to grab the credentials from the developer tools (maybe a JavaScript snippet that retrieves all three in an easily-copyable output)
* Figure out if there's a way to get `appSession` without having to look at a request by hand. Previously they used `directoryAccessToken` and `directoryIdentityToken`, which were available in the page cookies themselves (and thus via JavaScript in the console), rather than `appSession` on an outgoing request.
