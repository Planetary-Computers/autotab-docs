---
title: "Session"
description: "Overview of how sessions work in browsers and Autotab."
icon: "cookie"
---

# Session Overview

Session is the term used to describe data that is stored on your device by websites you visit. They use sessions to keep track of your login state, your preferences, and other data. If you've heard of "cookies", those are one way to store session data.

# Syncing Sessions

Autotab can securely sync your local session to your isolated cloud run environment, which allows Autotab to run without needing to re-login to most websites.

If you don't want to sync your session, or you need Autotab to access a site that requires you to log in every time, you can securely give Autotab access to the login credentials using [Secrets](/manual/secrets).

# How to Sync

Any time you run a skill, you can configure whether you want to sync your session. If you do, cloud Autotab will have the same login state as your local Autotab.

Scheduled runs will sync your session once when you create the schedule, but may need to refresh every once in a while (some sites ask you to log back in after a certain amount of time). There are two ways you can sync your session again:

1. Log in to the site in your local Autotab, then run the skill in the cloud and select "Sync Session".
2. Log in to the site in your local Autotab, then go to settings and enable the developer API. You'll now see a "Sync Session" button.
