# -*- coding: utf-8 -*-
git --version # git 版本

# 基本操作
cd
pwd 
ls (-a  -al)
mkdir
touch 
cp 
mv # 更改名稱
rm 
rmdir # 刪除空目錄
clear
cd /tmp
cd ..
* # for all

# vi 操作
normal to insert: i,a,o
insert to normal: esc,ctrl+[
exit: :w,:q,:wq
enter:vi,git commit

# user setting
git config --global user.name "Eddie Kao" # 全域設定
git config --global user.email "???"
git config --list # 查看使用者設定
git config --local user.name Sherly # local
git config --local user.email sherly@5xruby.tw
git config --global core.editor emacs # 預設編輯器從 Vim 轉為 Emacs
git config --global alias.co checkout # 把 git checkout 改為 git co
git config --global alias.br branch
git config --global alias.st status
git config --global alias.l "log --oneline --graph"
git config --global alias.ls 'log --graph --pretty=format:"%h <%an> %ar %s"'

# 進行版本庫處理
git init # 針對所在資料夾進行版本處理
git status # 現在 git 的狀態
echo "hello, git" > welcome.html 
git add welcome.html # 增加檔案到 staging area/ index 暫存區中
git add *.html
git add --all # add 全部 in git 版本庫中全部
git add . # add 全部 in 現在目錄位置下
git commit -m "init commit" # 把暫存區指令存到倉庫，後面為本次更動名字
git commit --allow-empty -m "空的" # 上傳空的 commit
git add -p index.html # 增加一部份的內容至暫存區

# 工作位置：工作目錄 Working Directory / 暫存區域 Staging Area / 儲存庫 Repository
git commit -a -m "update content" # 針對已存在的檔案直接 add and commit
git log # 觀看 git repository 的紀錄
git log --oneline
git log --oneline --graph # 更為精簡的 git repository 的紀錄
git log --oneline --author="Sherly" # 觀看 Sherly 執行的紀錄
git log --oneline --author="Sherly\|Eddie" #觀看 Sherly 或 Eddie 執行的紀錄 
git log --oneline --grep="h" # 找訊息中尋特定字
git log -S "Ruby" # 在檔案中尋找特定字
git log --oneline --since="9am" --until="12am" --after="2017-01" #從 2017 年 1 月之後，每天早上 9 點到 12 點的 Commit
git log welcome.html # 檢視特定檔案的歷史紀錄
git log -p welcome.html # 修改檔案細節
git show-branch # 查看 loacl branch 的紀錄
git show-branch -r
git show-branch -a


# 對 git 的修改、忽略、加入、查詢
git commit --amend -m "Welcome To Facebook" # 修改最後一次的訊息內容（算是重新commit）
git commit --amend --no-edit # 補充變更：暫存區內還有剛剛忘了更動的檔案，用此方法補充commit，而且不編輯 commit
# 空目錄無法被讀取，可在目錄裡加入 .keep 或 .gitkeep 檔讓 Git 發現目錄存在
# .gitignore 可以將某些檔案排除上傳至 git 中，另外記得這對已經在 git 裡的檔案無效，要先 git rm --cached 再 ignore
git add -f "filename" # 無視 ignore 強迫加入
git clean -fX # 強制刪除

# 資料回溯
git blame index.html # 發現檔案每一行寫的時間
git blame -L 5,10 index.html # 只看 5~10 行
git checkout cinderella.html # 救回尚未上傳到 git 但不小心刪掉的檔案
git checkout HEAD~2 welcome.html # 拿兩個版本前的內容
git reset "HEAD^" # 回溯至 特定編碼、抬頭 eg.e12d8ef~5，Head^ 表示將指標轉回前一次的狀態
git reset e12d8ef --hard # 可以 reset 到剛剛沒拆掉的檔案
git reset --mixed # reset 有三種模式，--mixed 是把刪掉的檔案放回工作區，--soft 是把刪掉的檔案放回工作區與暫存區， --hard 則是都丟掉
git reflog # 紀錄 head 的移動
git log -g # 同上，但更詳細

# 刪除檔案範例
rm welcome.html # 可以用 git status 觀看狀態喔 
git add welcome.html
git commit -m "刪除 welcome"
git rm welcome.html # 等於 做事＋add，移除也可以換成改名 mv
git rm welcome.html --cached # 從 git 中移除檔案，但該檔案還保留在 local

# head：目前所在的分支
cat .git/HEAD # 現在 HEAD 的指向
cat .git/refs/heads/master # 現在 master 的編號


# 分支 branch
git branch # 現在有哪些 branch
git branch cat # 創造 cat branch
git branch -m cat tiger # cat branch 改名成 tiger branch
git branch -d dog # 刪除 dog branch (git branch -D dog 則是強制刪除)
git checkout cat # 切換到 cat branch
git checkout -b sister # 新增並切換到 sister branch
git branch bird 657fce7 # 請幫我用在 657fce7 這個 Commit 上開一個叫做 bird 的分支
git checkout -b bird 657fce7 # 新增並切換到這裡
git branch -r # 觀看 remote上所有分支
git granch -l # 觀看 loacl 上所有分支
git branch -a # 觀看所有分支

# 合併分支 merge branch
# merge 把你的東西抓過來，所以你不變我變
git checkout master
git merge cat # 將 master 合併到 cat，merge 可以想成把現在的指標移動到 cat 的指標
# 要分清楚有 Fast Forward 與沒有這個的結構
# 同一條線上用 Fast Forward： 直接將舊標籤貼過去
# 不同線上：一個一個對照轉換過去
git merge cat --no-ff # 同一條線上還是想要一個一個轉換過去
git branch new_cat b174a5a #直接幫我建立一個叫做 new_cat 的分支，讓它指向 b174a5a 這個 Commit
git rebase dog #我，就是 cat 分支，我現在要重新定義我的參考基準，並且將使用 dog 分支當做我新的參考基準
git reset ORIG_HEAD --hard # 強制回到上次危險時機（合併 or rebase）

# 合併衝突
git rebase --continue # 萬一有rebase有合併衝突，用這個再跑一次
git checkout --ours cute_animal.jpg # 合併衝突使用我方的內容，記得 commit
git checkout --theirs cute_animal.jpg # 合併衝突使用對方的內容，記得 commit

git rebase -i xxxxxx # 回到某次指令狀態，會進入 Vim 介面，重新做出 commit ，也就是針對 commit 進行操作
git reset ORIG_HEAD --hard # 取消 rebase
# 可在 rebase 的 Vim 介面執行 edit ，讓 base 執行指到該介面，在對那時進行調整
git revert HEAD --no-edit # 取消這次的commit 回到上次的 commit，但保留這次移動紀錄

# tag 標籤
git tag big_cats 51d54ff # 在 51d54ff 的 commit 上貼上 big_cats 的標籤，指向 commit  # lightweight 輕量標籤
git tag big_cats 51d54ff -a -m "Big Cats are comming" # annotated 標註用標籤 ，清楚紀錄誰在什麼時候貼的，用在版本更新等重要資訊，指向tag物件
git show big_cats # 打開標籤資訊 
git tag -d big_cats # 刪除標籤

# 儲存進行到一半的工作
git stash # Untracked 狀態的檔案預設沒辦法被 Stash，需要額外使用 -u 參數。
git stash list # 查看 stash list
git stash pop stash@{2} # 回到 stash@{2} 的工作狀態，同時刪除該 stash
git stash drop stash@{2} # 刪除 stash@{2}
git stash apply stash@{0} # 回到 stash@{2} 的工作狀態

# 一次處理大量 commit / 刪除某個東西 on git
git filter-branch --tree-filter "rm -f config/database.yml" # 修改全部的 commit
git reset refs/original/refs/heads/master --hard # 復原 filter 掉的東西
git filter-branch -f --tree-filter "rm -f config/database.yml" # 強制斷乾淨
rm .git/refs/original/refs/heads/master # 移除備份點
git reflog expire --all --expire=now # 讓 reflog 立刻過期
git fsck --unreachable # 查看 unreachable 的物件
git gc --prune=now # 使用 git 的資源回收機制
git push -f # 強制推送現在的資料（覆蓋掉）

git cherry-pick 6a498ec # 複製某次 commit 的內容到現在的 head，並 commit 起來
git cherry-pick fd23e1c 6a498ec f4f4442 # 複製好幾次 commit 的內容到現在的 head，並 commit 起來
git cherry-pick 6a498ec --no-commit # 撿過來的動作放在暫存區，不 commit

git branch --remote # 目前的遠端分支 或者用 -r
git checkout -t origin/refactoring # 針對斷頭的遠端分支連結 -t == -track
git checkout refactoring # 用完上面那個，後面檔案就在本地的 track 裡了


# push、pull 到 github 上
echo "# git-practice" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/sakutarou/git-practice.git # git 加入遠端節點，名叫 origin，位置是後面那串網址
git push -u origin master:main # 將手邊的 master 分支內容推向 origin，並命名為 main 分支
# -u 用來設定上游 upstream，簡單說就是設定 main 的前面固定接 master，本地 master 的 upstream 是 main

git fetch # 將 remote 的更新抓下來
git merge origin/master # 把本地的 head 與 master 合併到 fetch 下來的 的 origin/head, origin/master
git pull = git fetch + git merge
git pull --rebase # 以 rebase 而非 merge 的方式進行合併

git clone git@github.com:kaochenlong/dummy-git.git hello # 從網路上複製版本庫下來，並將目錄取名為 hello

# 多人協作
git pull --rebase # 先拉再推
# git push -f # 直接不理別人的指令蓋掉 
git remote #　現在有哪些遠端操作
git remote -v # 更詳細
git remote add dummy-kao https://github.com/kaochenlong/dummy-git.git # 新增遠端節點（有點類似網路上的add）
git push origin :cat # 把線上 cat 的分支刪除
git push -f origin features/my_branch # 強制將以 my_branch 為主並推上 origin， github 有 protection setting 的選項

# 建立靜態網頁
創建 repository 並定 "username".github.io 為名。
git add index.html
git commit -m "add index"
git remote add origin https://github.com/eddiekao/eddiekao.github.io.git
git push -u origin master

# 產生更新檔
git format-patch fd7cd38..6e6ed76 # 產生fd7cd38 這個 Commit 之後（不包括本身），直到 6e6ed76 這個 Commit 為止的更新檔
git format-patch -2 -o /tmp/patches # 產生最近兩次 commit 的更新檔，並放在 /tmp/patches
git am /tmp/patches/* # 使用更新檔

# git flow
Master 分支：穩定的上線版本
Develop 分支：所有開發人員的基礎分支
Hotfix 分支：現在運作的版本發生重大問題要立刻修復，做完後合併回 Master 與 Development
Release 分支：Develop 到一個段落，進行上 Master 前的最後測試，做完後合併回 Master 與 Development
Feature 分支：新增功能的試作品