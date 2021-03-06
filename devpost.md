# iLove
#### An anonymous interests purveyor

## Inspiration
Have you ever expressed an interest in a specific hobby, topic or genre but didn't know exactly how to find like-minded individuals? Introducing iLove - an anonymized interest app that allows you to find individuals near you (Within up to 50 miles!) to engage with, allowing you to find yourself individuals that you share interests with, with relative ease.

## What it does
After signing up for an account, anonymous or personal, the app takes care of the rest. You can easily add and remove interests through the app interface, and our app runs on both Android and iOS, ensuring full compatibility with any phone within the last few years. Your location is broadcasted, and stored, only when you wish it to be, allowing you to broadcast your interests at a specific time, allowing you to determine when you wish to participate in your interested subjects with others nearby. An example interest would be Huskies! Imagine someone says they have a Huskie as their interest and upon contact you are able to pet the dog!

## How I built it
The front-end side of the application was designed using React-Native, with the back-end being designed using Google's Infrastructure as a Service platform (Google Cloud Platform). Specifically, the backend uses Google Firebase and Firestore, with Cloud Functions allowing our app to have a server-less backend that can scale activities at will with no effort on our part. Additionally, we used the Google Maps API to allow access to locational data on the device and help find geolocation from Google's system. Future Google Maps API usage will include selection of places to help facilitate meeting locations for the anonymous individuals.

As for packages, react-native side we utilized react-native-maps to allow working with the Google Maps API, and designed much of our front-end using react-native. For Google Cloud Platform Cloud Functions we utilized Python and Flask, along with Google's firebase-admin sdk to help design the cloud functions and create our serverless backend.

## Challenges I ran into
Of the multitude of challenges we encountered at first, our major one was dealing with React-Native, which had a tendency to crash on us with no real understandable reason. Over time we were able to pinpoint some components that were designed "iffy" and therefore sometimes worked and sometimes didn't on the Android/iOS devices we used.

On the Google Cloud Functions side, it was difficult finding great documentation on firebase-admin, as most firebase usage is likely in JavaScript or Web requests, however I eventually was able to find a good enough documentation that the code is now to an acceptable level, and works 100% of the time.

## Accomplishments that I'm proud of
The best accomplishment in the creation of this app was being able to design not only a front-end but a back-end that was able to communicate through a common API Framework, allowing both teams (front/back) to work independantly of each other for most of the 36 hours. Despite several hiccups in development, both teams were able to collaborate through this API and produce the application within our timeframe.

## What I learned
For the front-end team, both individuals learned and developed a good understanding of Android Studio, specifically learning how to use the Android Emulator to help in facilitating that our app was running smoothly and effectively as we wished it to be.

For me (Nate Ruppert, author of readme), I didn't know anything of Firebase or Google Cloud Functions until after the start of this project. Both tools proved essential in developing a proper backend, and were great tools to learn to use and will definitely be used for future projects.

## What's next for iLove
iLove will continue being developed and matured, and will be given more new features such as locational meet-up setup, full geolocation customization (by time), and others.
