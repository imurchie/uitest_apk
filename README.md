# UITest

A very small Android app into which I can insert elements in order to test their automatability.

## Requirements

* [Android SDK](developer.android.com)

## Building

```shell
$ cd into/this/repo
$ ant debug
```

You can also run `ant debug install` to build and immediately deploy the app to a connected Android device or emulator.

## Installing

You can install the apk through the [Android Debug Bridge](http://developer.android.com/tools/help/adb.html).

To install:

```shell
$ cd into/this/repo
$ adb install bin/settings_apk-debug.apk
```

To uninstall:

```shell
$ adb uninstall io.appium.settings
```

## License

Apache License 2.0
