### Template Table of Contents

### OVERVIEW
- About splunk_apps
- Release notes
- Performance benchmarks
- Support and resources

### INSTALLATION
- Hardware and software requirements
- Installation steps 
- Deploy to single server instance
- Deploy to distributed deployment
- Deploy to distributed deployment with Search Head Pooling
- Deploy to distributed deployment with Search Head Clustering
- Deploy to Splunk Cloud 


### USER GUIDE
- Key concepts
- Data types
- Lookups
- Configure splunk_apps
- Troubleshooting
- Upgrade
- Example Use Case-based Scenario

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### OVERVIEW ###

#### About splunk_apps

| Author | James Donn |
| Author | Kristofer Hutchinson |
| Author | Chhean Saur |
| --- | --- |
| App Version | 1.0 |
| Vendor Products | Splunk 6.3 |
| Has index-time operations | false, need not install on indexers |
| Create an index | true, impacts disk storage |
| Implements summarization | false |

The splunk_apps allows a Splunk® Enterprise administrator to analyze web site content.  This App also provides examples of:
  Multi-search
  Various form options
  Custom CSS and js
  Custom data collection scripts

After being asked for a list of Splunk Apps in a spreadsheet a few times, I found a need to build this App.  This App provides a simple dashboard with App stats and allows 
you to search for Splunk Apps within Splunk. It was also designed to work if you are offline, as long as you have been online once to collect data.

Splunk 6.3 now has most of this built in, but the offline benefits of this App still make it useful.

This was a collaborative effort:
  James Donn - Dashboards and Searches
  Kristofer Hutchinson - Custom CSS and .js
  Chhean Saur - Data Collection script


##### Scripts and binaries

$SPLUNK_HOME/etc/apps/splunk_apps/bin/getSplunkApps.py runs every hour to collect the latest list of Splunk Apps.  It is designed to work for up to 2,100 Apps on 
SplunkBase.  After that point, some minor updates to the script and dashboard will be needed.  

#### Release notes
This is the initial release, everything is new.

##### About this release

Version 1.0 of the splunk_apps is compatible with:

| Splunk Enterprise versions | 6.3 |
| --- | --- |
| CIM |  |
| Platforms | Platform independent |
| Vendor Products | Splunk |
| Lookup file changes |  |

##### New features

Splunk_apps includes the following new features:

- N/A

##### Fixed issues

Version 1.0 of splunk_apps fixes the following issues:

- N/A

##### Known issues

Version 1.0 of splunk_apps has the following known issues:

- The “New Apps Compared to Last Week” dashboard panel will not have enough information in it to show trends until you have collected data for a week.  This is only
because you have not yet collected the data to draw the entire contents of the dashboard.  

##### Third-party software attributions

Version 1.0 of splunk_apps incorporates the following third-party software or libraries.

- None

#### Performance benchmarks

This dashboard uses two multi-searches to speed them up.  I left the original dashboard there, so that you can see how much faster it loads with multi-search implemented.

##### Support and resources

**Questions and answers**

Access questions and answers specific to splunk_apps at http://answers.splunk.com.

**Support**

You can email jim@splunk.com with any comments, questions, or concerns.  


### INSTALLATION AND CONFIGURATION ###

### Hardware and software requirements

#### Hardware requirements

Splunk_apps supports the following server platforms in the versions supported by Splunk Enterprise:

- All

#### Software requirements

To function properly, splunk_apps requires the following software:

- None

#### Splunk Enterprise system requirements

Because this add-on runs on Splunk Enterprise, all of the [Splunk Enterprise system requirements](http://docs.splunk.com/Documentation/Splunk/latest/Installation/Systemrequirements) apply.

#### Download

Download splunk_apps at https://splunkbase.splunk.com.

#### Installation steps

To install and configure this app on your supported platform, follow these steps:

1. Download the App
2. Install it through the Splunk UI
3. There is no step 3!

##### Deploy to single server instance

Follow these steps to install the app in a single server instance of Splunk Enterprise:

Same as above.

##### Deploy to distributed deployment

**Install to search head**

##### Deploy to distributed deployment with Search Head Pooling

Basic installation.

##### Deploy to distributed deployment with Search Head Clustering

Basic installation.

##### Deploy to Splunk Cloud

Basic installation.


### USER GUIDE ###

### Key concepts for splunk_apps

Details of any key concepts a user must be cognizant of in order to configure and use the app.


### Data types

This app provides the index-time and search-time knowledge for the following types of data from <N/A>:

Description and example

N/A

Description and example

N/A

These data types support the following Common Information Model data models:

N/A

### Lookups

The splunk_apps contains 0 lookup files.


Description of what the lookup does.

- File location: N/A
- Lookup fields: N/A
- Lookup contents: N/A

### Configure splunk_apps

None.

### Troubleshoot <splunk_apps>

***Problem***
Script does not run, so there is no data.

***Cause***
Permissions?

***Resolution***
To test the script, manually run it as the user that runs Splunk.  Adjust permissions as necessary.


### Upgrade splunk_apps
N/A

### Example Use Case ###
You have Splunk on your laptop and you are in a meeting where someone asks, "Does Splunk have an App for that?".  The problem is that you do not have wireless
access because it is down, or you are a visiting guest.  Just launch up this App and search away.  

