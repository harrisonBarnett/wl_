# wl_

## Welcome to the repository for wl_, a simple olympic weightlifting progression tracking application.
![the wl_ app landing page](https://i.imgur.com/2nEUKaK.png)

Most of us are familiar with the functionality of a typical fitness or exercise tracker. They usually give you a movement
and prescribe a set x rep scheme. However, many fall short when it comes to actually advising the user as to how to 
progress the amount of weight to use. To that end, I have made wl_, an MVC application built in Flask. 

Here is the main page once a user logs in:
![the main page](https://i.imgur.com/oWZtM5x.png)

From here, the user must configure their application by providing their one-rep-max values in the options page:
![the options page](https://i.imgur.com/S3QXwb5.png)

Once the application is configured, the user can log into the app from any device and access a bespoke, linearly-progressed 
olympic weightlifting program. 

The user is expected to complete each session (squat, snatch, clean & jerk and snatch / clean & jerk) within a cycle. A cycle
may be any arbitrary (and reasonable) amount of days. Once the user chooses a session to engage in, a set x rep scheme is 
generated with weights based on a percentage of the one rep max provided in their app configuration:

![session page](https://i.imgur.com/NVE0Wjd.png)

### Progression occurs in two ways:
If the user does not complete every repetition prescribed in a session, they will select "miss," in which case nothing 
happens and the user can try again next cycle. However, if the user chooses "make" during their **snatch / clean & jerk** session 
then some logic runs in the backend to progress the relevant one rep max by a reasonable percentage. 

However, if the user chooses "make" during their **squat** session, a seperate, slightly more complex algorithm runs in the
backend. This is because there is a squat progression based on a four session subcycle nested within the broader scope of the
application. 

The squat progression is based on the popular 5/3/1 powerlifting progression which prescribes a session consisting
of 3 sets at 5 reps, a session consisting of 3 sets at 3 reps, a session consisting of 3 sets at 5 reps, 3 reps and 1 rep and a 
session consisting of 3 sets at 5 reps at a very low weight to serve as a deload. These sessions will progress based on the
user's ability to complete the prescribed repetitions until they get to the third subcycle (e.g. 3 sets at 5, 3 and 1 reps). Once
the "make" condition is met here, then the user's one rep max for their squat is increased by a reasonable percentage.

In short, the user sets the pace for how quickly their weights will increase over time while secretly running a 5/3/1 program
to ensure a strong, confident squat. 

This application is not meant to teach the olympic lifts to beginners, as it it assumed that any user has either a reasonable
command of the classic lifts or access to a coach. This application exists as a tool for the amateur or novice olympic weightlifter 
to easily progress their weights without the need for spreadsheets or physical notebooks. 

Happy lifting!

