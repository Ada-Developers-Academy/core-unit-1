# Activity: Git History

<!-- Written to be synchronous -->
<!-- Ideal Format: Small groups -->

## Goal

Our goal is to practice the process of making commits as a group. We will also practice collaborating in Git as a group.

Our goal is to practice this without actually typing and running these commands in the terminal; however, we should practice recognizing what commands we _would_ type.

## Activity Instructions

Assemble into small groups.

For each part,

1. Read through the setup directions
1. Setup as a group
1. Read through the instructions
1. Complete the instructions

### Preparation

Part 1 and Part 2 are a combination of discussion and individual writing:

- Each individual should have note-taking materials
- Bring up any Git references, resources, lessons, and notes

## Part 1

In part 1, each group member will describe the steps to create a specific commit, and diagram what Git "looks like" at each step.

Each member will pick one of the commits in the Setup section. These specific commits already have these details:

- The number and names of files that contain changes
- The commit message
- The commit hash

The group members will use these details to name the specific commands needed.

### Part 1 Setup

1. Begin a diagram of Git's areas. Each individual should draw in their own notes a...
   - box labeled "Untracked Changes Area"
   - box labeled "Local Changes Area"
   - box labeled "Staging Area"
   - box labeled "Git Log"
1. Each individual should pick one of these commits:

| Commit Hash | Commit Message                                  | Modifies files                                       | Adds new files            |
| ----------- | ----------------------------------------------- | ---------------------------------------------------- | ------------------------- |
| `1a91c`     | "refactors plan_trip() to for loop"             | `plan.py`                                            | -                         |
| `2e7de`     | "adds ability to plan multi-day hikes"          | -                                                    | `plan.py`, `test_plan.py` |
| `384ca`     | "deletes outdated mentions of weather advisory" | `report.py`, `test_report.py`                        | -                         |
| `4o5em`     | "renames supplies to supply                     | `supplies.py`                                        | `supply.py`               |
| `5JTrA`     | "adds error handling when loading hike data"    | `hike.py`, `test_hike.py`, `list.py`, `test_list.py` | -                         |
| `6ee9f`     | "replaces hike report text with new copy"       | `report.py`, `test_report.py`, `hike.py`             | -                         |

### Instructions

Group members will take turns making one step. During your turn, you should say out loud what your step is, and the Git command that goes with it. Each group member should collaborate, discuss, help, and confirm that the other group members are on the right track.

These are the steps:

1. Using the information from your selected commit, write down a new file in "Untracked Changes" or a modified file in "Local Changes"
1. Repeat step 1 until there are no more files to name
1. Move a file into "Staging," and erase it from its previous area
1. Repeat step 1 until there are no more files to add to staging
1. Create a commit with the specified commit message
1. Write down the commit's commit hash in the "Log"

## Part 2

Imagine your group is a dev team that works on the product Hike Planner.

Repeat the same process described in Part 1. However, the goal for part 2 is to describe the steps to pull and push commits, and diagram what Git "looks like" at each step.

Each member will pick one of the commits in the Setup section. The only detail provided for these commits is the commit hash.

### Part 2 Setup

1. Make a diagram that represents a team's repo. Label this "Hike Planner Git Log." Ensure all members can see this.
1. Begin an individual diagram that represents each member's own laptop. Each individual should draw a box labeled "Git Log."
1. Fill in the "Hike Planner Git Log" box with these commit hashes:
   - ```
     43d8f
     01a6b
     882ca
     c6f7p
     ```
   - The commits are ordered reverse-chronologically. Commit `43d8bf` is the newest commit. `c6f79p` is the oldest commit.
1. Each individual should pick one of these commit hashes:
   - ```
     1a91c
     2e7de
     384ca
     4o5em
     5JTrA
     6ee9f
     ```

### Instructions

Each group member should take turns making one step. Each group member should collaborate, discuss, help, and confirm that the other group members are on the right track.

1. "Clone" the repo.
   - Copy the Git Log from the team repo into the individual Git Log box.
1. Make your commit.
   - Add your commit hash to the top of your individual Git Log. (Since it is the newest, it should go on top)
1. "Push" to the team repo:
   1. First, you **must** "pull" from the team repo. Check if there are any new commits on the team's Git Log. Copy new commits to your own Git Log, and make your Git Log identical.
   1. Write down your commit hash back to the top of your individual Git Log.
   1. Add your commit hash to the top of the Hike Planner Git Log.
1. Once everyone has successfully pushed their commit, pull from the team repo.

## How to Review

Consider what you observed during this activity.

In Part 1:

- What common traits did the commit messages have?
- Between the commits, when was the process of making a commit different? What caused those differences?
- Did anyone come up with a way to make this process "stick," with a metaphor, mnemonic, diagram, or something else?

In Part 2:

- How would you describe the relationship between the team's Git Log vs. your individual Git Log?
- Predict: What are the advantages of pulling new commits often?
