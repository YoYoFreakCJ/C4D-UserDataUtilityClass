# Introduction
When working with user data I was bummed out by all the boilerplate code. So I made a wrapper to help me out. Experience when working with Python is required.

# Usage
Copy the contents of UserData.py into your script. The file defines the class `UserData`. Use it by calling the static `Create` function:

```lang:Python
userData = UserData.Create(myObj, myUserDataId)
```

The first parameter is the object which holds the user data which can be any base object or the user data tag.

Right now the following functions are implemented:

|Function|Description|Usage|
|-|-|-|
|Hide|Hides the user data.|`userData.Hide()`|
|Show|Show the user data.|`userData.Show()`|
|GetValue|Gets the user data value.|`myValue = userData.GetValue()`|
|SetValue|Sets the user data value.|`userData.SetValue(myValue)`|
