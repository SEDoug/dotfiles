# Usage: for Kali and Ubuntu

# -r arguments | listing (-l) format
# list all (-a) files — | including hidden files
# print the file sizes in human-readable (-h) formats
# alias ls='ls --color=always -rthla'

# Reminder to make sure to have this in your .bashrc to activate .bash_aliases
#  if [ -f ~/.bash_aliases ]; then
#      . ~/.bash_aliases
#  fi

# Adding function here for automation

function apt-updater {
        apt-get update &&
        apt-get dist-upgrade -Vy &&
        apt-get autoremove -y &&
        apt-get clean
        }
#       reboot

# Always enable colored `grep` output
# Note: `GREP_OPTIONS="--color=auto"` is deprecated, hence the alias usage.
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

# Shortcuts
alias ls='ls --color=always -rthla'
alias reload="source ${HOME}/.bashrc"
alias ch='history | grep git'
alias dush=' du -sh "$@"* | sort -h'
alias hg='history | grep'
alias lah='ls -lah'
alias yt='code ~/Google\ Drive/YouTube/Scripts/'
alias cyt='cd ~/Google\ Drive/YouTube/Scripts/'
alias oyt='xdg-open ~/Google\ Drive/YouTube/Scripts/'

# Adding hacking aliases here
alias hackwifi='bsside-ng -vv wlan0'
