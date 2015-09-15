#!/usr/bin/env bash

SESSIONNAME="fearMe"
tmux has-session -t $SESSIONNAME &> /dev/null

if [ $? != 0 ] 
 then
    tmux new-session -s $SESSIONNAME -n main -d
    tmux send-keys -t $SESSIONNAME "~/Desktop/code/fearMe/Scripts/runme.sh" C-m 
fi

#tmux attach -t $SESSIONNAME
