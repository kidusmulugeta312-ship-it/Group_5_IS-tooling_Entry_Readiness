# Upload and submission(generalized guide for collaborators only)
1. Download and extract the starter ZIP from telegram. Open its main folder to see README.md and the nine required folders.
2. Review proposed roles, privacy, and drafts. The original proposal PDF contains student IDs. Agree on public/private visibility with your group and instructor before uploading.
3. Sign in to YOUR GitHub account. Click + > New repository. Select your account as owner. Suggested name: group5-is-tooling-readiness. Do not initialize README, .gitignore, or a license, since starter files already exist. Create repository.
4. On the empty repository page, choose uploading an existing file. Drag the CONTENTS of the extracted main folder into the upload area (not the ZIP, and not its outer wrapper folder). Verify README.md and all nine folders will be at the repository root.
5. Commit with an honest message: Initialize project structure, proposal, and draft instruments. Do not claim that the pilot or study is complete.
6. If your browser omits hidden files, create .gitignore separately using the supplied text. It must be named exactly .gitignore.
7. Review the README on GitHub. Confirm all required folders are visible. Resolve proposed roles and privacy concerns before treating this as submission-ready.
8. Copy the repository URL from your browser. On Google Classroom open the correct assignment and paste the URL as directed. If Add or create > Link is available, add it there; then Turn in or Submit if the assignment requires it. Check confirmation. A comment alone may not be the required submission route.
9. If private, grant the instructor access using the instructor's confirmed GitHub username. Verify access before the deadline. Do not guess the username.
10. Invite group members through repository Settings > Collaborators (the wording may vary with account type), using their verified GitHub accounts.
11. Make genuine commits throughout the project. Keep the original proposal unchanged; place revised versions beside it. Never fabricate prior history to satisfy the evolution requirement.

The stated link deadline is November 25, 2026. The separate three-days-after-announcement requirement cannot be checked without the actual announcement date. This ZIP alone is not a hosted GitHub repository and does not submit anything to Classroom.

## Optional command-line upload instead of browser upload
Run from the extracted main folder. Replace YOUR-USERNAME with your actual account name and ensure the repository name matches the empty repository you created.

```sh
git init
git branch -M main
git add .
git commit -m "Initialize project structure, proposal, and draft instruments"
git remote add origin https://github.com/YOUR-USERNAME/group5-is-tooling-readiness.git
git push -u origin main
```
Use GitHub's authentication flow when prompted; do not put tokens or passwords in repository files. If Git asks for an author identity, set your real chosen Git name and appropriate email before committing. This creates a new repository history starting with your actual upload, not historical evidence of earlier work.

## Official documentation
- https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
- https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github
  These are the steps used to create the repo.One member is enough for creating the repo, i will create one and add all of the collaborators. if u face any problem we can meet and solve the issue.
