---
title: "Debugging GA4 on mobile apps and Android WebView screens"
date: "2024-11-18T16:33:31.811Z"
draft: false
tags: []
source: "beehiiv"
original_url: "https://blog.giancampo.com/p/debugging-ga4-on-mobile-apps-and-android-webview-screens"
---

## Table of Contents

1. [Debugging GA4 on mobile apps](#debugging-ga-4-on-mobile-apps)

   1. [Setup process](#setup-process)
   2. [Debugging session](#debugging-session)
2. [Debugging GA4 on web pages from mobile devices](#debugging-ga-4-on-web-pages-from-mo)

   1. [Setup process](#setup-process)
   2. [Debugging session](#debugging-session)
3. [Debugging GA4 on hybrid apps with WebView screens](#debugging-ga-4-on-hybrid-apps-with-)

We’ve found a high amount of traffic in our GA4 properties coming from mobile devices, web platform thus decided to debug the current implementation, considering we’ve inherited it from another consulting agency and then several app releases have been pushed in the meanwhile.

The idea was to simulate traffic from the mobile app going to WebView screens and see if the app\_instance\_id - as recommended by Google - was cut causing GA to associate the WebView views to new sessions and users.

## Debugging GA4 on mobile apps

Here the best tool to use is Analytics Debugger for Apps by David Vallejo <https://analytics-debugger.com/tools/analytics-debugger-for-apps/>

There are two main steps to consider when debugging mobile apps: 1) The setup process. 2) The debugging session itself.

### Setup process

1. After the installation is done, this will be the screen you’re going to see, where you can click on the Android icon to add a device

   ![](img-01-69b0bf.jpg)
2. In the coming screen, click the option “Link new Android device”

   ![](img-02-100ff8.jpg)
3. Then you can pair the device of your choice with the application by clicking on “Pair Device With QR Code”

   ![](img-03-0d0f36.jpg)
4. But first, you should make sure your device has the Wireless Debugging option enabled in the Developer Options settings (System settings). This step requires your mobile device and desktop PC both connected to the same Wi-Fi network

   ![](img-04-2b459d.jpg)
5. You will be asked if you want to allow the Wireless debugging and you can decide if you want to flag the options always allowing the pairing in your Wi-Fi network

   ![](img-05-67fd2d.jpg)
6. With that, you should also click on the option Wireless debugging where you can click on Pair device with QR code and then scan the QR provided by the Analytics Debugger for Apps

   ![](img-06-84fc28.jpg)
7. Finally, the Analytics Debugger for Apps will ask for the port you can find again in the Wireless debugging settings after the “:”, in my example “40995”

   ![](img-07-9da8ba.jpg)

### Debugging session

1. Now, you will see the application UI gives you the chance to Select your device. Just click on Select to actually start the debugging session, and then Next in the bottom right corner of the UI

   ![](img-08-043d5a.jpg)
2. You will see a complete list of apps you can debug. Just choose yours and click on Debug, and then Start Debugging in the bottom right corner of the UI. You can even search the app of your choice easily digiting some words in the Package ID search bar

   ![](img-09-0452aa.jpg)
3. Now open the app you’ve chosen on your device and interact with it. In case a Firebase implementation is there, you’re going to see the screen of Analytics Debugger for Apps populated with details about the events recorded, as follows

   ![](img-10-c9829d.jpg)
4. The debugging session will also show you the events tracked in the GA4 DebugView, if the implementation has been done correctly

   ![](img-11-259687.jpg)
5. In my case I just wanted to take note of the app\_instance\_id, so I got to the Shared Payload section of the UI

   ![](img-12-e5632e.jpg)

## Debugging GA4 on web pages from mobile devices

For Android, there’s a document by Google <https://developer.chrome.com/docs/devtools/remote-debugging?hl=en>

Also for this case, the two main steps to accomplish are again a setup and the debugging itself.

### Setup process

1. First things first, you should enable USB debugging in Systems Settings

   ![](img-13-7cf3fd.jpg)
2. And of course, you really want it clicking OK in the dialog

   ![](img-14-89a307.jpg)
3. Go to your Chrome on the PC you’re working and get to chrome://inspect#devices (try pasting it in the address bar, if you don’t know how to do that)
4. Be sure the Discover USB devices option is ticked

   ![](img-15-6f4611.jpg)
5. Now use a USB cable to connect your mobile device to the PC you’re working on. Make sure you don’t use a USB Hub since I actually encountered some issues when trying it and even Google recommends against doing so
6. If everything’s OK, you’ll see your device listed in Chrome (mine is RMX19993, do not consider the first one which is another connection)

   ![](img-16-65d116.jpg)

### Debugging session

Starting the debugging session is pretty easy: Open up your Chrome in the Android device: You’ll see it logged in Chrome where you now can perform an inspection using DevTools.

![](img-17-965eb3.jpg)

For instance, in the screenshot below you can see I have a web page open and a new blank tab.

If you now click on inspect you’ll be taken to Chrome DevTools where you can debug GA4 by using the good old method of having a look at HTTP calls to GA in the Network tab.

![](img-18-16adba.jpg)

## Debugging GA4 on hybrid apps with WebView screens

Getting back to what I actually needed, I decided to connect my device with both Analytics Debugger for Apps (from now on, ADFA) and the USB debugging.

That’s why I started a debugging session with ADFA and then had a look at Chrome DevTools to find if the app\_instance\_id was available in the WebView screen.

Here below you can see the parameter I needed in the Shared Payload section:

![](img-19-ebd042.jpg)

Then from my mobile device, I got to the WebView screen and here you can see Chrome recognizing it.

![](img-20-530fab.jpg)

And from there I checked if the app\_instance\_id was available in the payload sent to GA4. Unfortunately it wasn’t there, but that’s another story.

![](img-21-23b161.jpg)

That’s it, this is how I recommend debugging apps and WebView screens. Please let me know in the comments if you have anything to add or questions.
