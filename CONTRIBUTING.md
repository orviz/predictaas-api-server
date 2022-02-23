# Release policy.

## 1. Desing a kanban project from scratch to the first release and a new one between releases.

## 2. First release version starts from 1.0.0.
	2.1. Semantic Versionin standard is followed (x.y.z).
		2.1.1 x is a mayor release: has changes that may be incompatible with prior major releases.
		2.1.2 y is a minor release: adds new functionality and bug fixes in a backwards
		compatible manner.
		2.1.3 Z is a patch release: adds backwards compatible bug fixes.

## 3. kanban is composed by 5 columns:
	3.1 To do:
	3.2 In progress:
	3.3 Review in progess
	3.4 Reviewer approved
	3.5 Done

# Workflow Process
You should follow the GitFlow workflow for contibuting with this project, which is summed up below:

## 1. Create a branch
Create a branch in your repository. A short, descriptive branch name enables your collaborators to see ongoing work at a glance. When creating the branch, use the following naming codes:

- docs/: contributions in the documentation
- bugfix/: contibutionsfor fixing bugs
- feature/: change for adding new features

By creating a branch, you create a space to work without affecting the default branch. Additionally, you give collaborators a chance to review your work.

## 2. Make changes

On your branch, make any desired changes to the repository. 

Your branch is a safe place to make changes. If you make a mistake, you can revert your changes or push additional changes to fix the mistake. Your changes will not end up on the default branch until you merge your branch.

Commit and push your changes to your branch. Give each commit a descriptive message to help you and future contributors understand what changes the commit contains. For example, fix typo or increase rate limit.

Ideally, each commit contains an isolated, complete change. This makes it easy to revert your changes if you decide to take a different approach. 

By committing and pushing your changes, you back up your work to remote storage. This means that you can access your work from any device. It also means that your collaborators can see your work, answer questions, and make suggestions or contributions.

Continue to make, commit, and push changes to your branch until you are ready to ask for feedback.

Tip: Make a separate branch for each set of unrelated changes. 

## 3. Create a pull request

Create a pull request to ask collaborators for feedback on your changes. Pull request review is very valuable as this repository requires 2 approving reviews before pull requests can be merged. When you create a pull request, include a summary of the changes and what problem they solve. In addition to filling out the body of the pull request, you can add comments to specific lines of the pull request to explicitly point something out to the reviewers.

## 4. Address review comments

Reviewers should leave questions, comments, and suggestions. Reviewers can comment on the whole pull request or add comments to specific lines. You and reviewers can insert images or code suggestions to clarify comments. For more information, see "Reviewing changes in pull requests."

You can continue to commit and push changes in response to the reviews. Your pull request will update automatically.

## 5. Merge your pull request

Once your pull request is approved, merge your pull request. This will automatically merge your branch so that your changes appear on the default branch. GitHub retains the history of comments and commits in the pull request to help future contributors understand your changes. For more information, see "Merging a pull request."


## 6. Delete your branch

After you merge your pull request, delete your branch. This indicates that the work on the branch is complete and prevents you or others from accidentally using old branches. 

For more information, see review the Github Flow documentation.
