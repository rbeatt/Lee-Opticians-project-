#############################################################################
# Generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#  Mar 14, 2021 02:20:16 PM GMT  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { \
    leeopticianslogo_jpg "../Users/ryanb/OneDrive - C2k/A2 2020-2021/Computer Science/A2 Unit 5/Code/LeeOpticianslogo.jpg" \
}
vTcl:create_project_images $image_list   ;# In image.tcl


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m45" -background #ffffff 
    wm focusmodel $top passive
    wm geometry $top 600x716+394+0
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1370 749
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    wm title $top "Order Form"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    menu $top.m45 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    frame $top.fra46 \
        -borderwidth 2 -relief groove -background #ffffff -height 406 \
        -width 125 
    vTcl:DefineAlias "$top.fra46" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra46
    button $site_3_0.but60 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Add 
    vTcl:DefineAlias "$site_3_0.but60" "AddBtn" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but61 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Search 
    vTcl:DefineAlias "$site_3_0.but61" "SearchBtn" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but62 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Delete 
    vTcl:DefineAlias "$site_3_0.but62" "DeleteBtn" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but63 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Update 
    vTcl:DefineAlias "$site_3_0.but63" "UpdateBtn" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but64 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Print Invoice} 
    vTcl:DefineAlias "$site_3_0.but64" "PrintBtn" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but65 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$site_3_0.but65" "Button6" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but66 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Close Form} 
    vTcl:DefineAlias "$site_3_0.but66" "CloseBtn" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.but60 \
        -in $site_3_0 -x 0 -relx 0.24 -y 0 -rely 0.049 -width 63 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but61 \
        -in $site_3_0 -x 0 -relx 0.24 -y 0 -rely 0.172 -width 66 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but62 \
        -in $site_3_0 -x 0 -relx 0.24 -y 0 -rely 0.296 -width 64 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but63 \
        -in $site_3_0 -x 0 -relx 0.24 -y 0 -rely 0.419 -width 69 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but64 \
        -in $site_3_0 -x 0 -relx 0.16 -y 0 -rely 0.542 -width 87 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but65 \
        -in $site_3_0 -x 0 -relx 1.12 -y 0 -rely 0.714 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but66 \
        -in $site_3_0 -x 0 -relx 0.16 -y 0 -rely 0.887 -width 91 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    entry $top.ent47 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 314 
    vTcl:DefineAlias "$top.ent47" "OrderIDEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent48 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 314 
    vTcl:DefineAlias "$top.ent48" "OrderDateEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent49 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 314 
    vTcl:DefineAlias "$top.ent49" "SupplierIDEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent50 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 314 
    vTcl:DefineAlias "$top.ent50" "ProductIDEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent51 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 314 
    vTcl:DefineAlias "$top.ent51" "QuantityEntry" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab53 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text OrderID 
    vTcl:DefineAlias "$top.lab53" "OrderIDLabel" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab55 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text OrderDate 
    vTcl:DefineAlias "$top.lab55" "OrderDateLabel" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab56 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text SupplierID 
    vTcl:DefineAlias "$top.lab56" "SupplierIDLabel" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab57 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text ProductID 
    vTcl:DefineAlias "$top.lab57" "ProductIDLabel" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab58 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Quantity 
    vTcl:DefineAlias "$top.lab58" "QuantityLabel" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab59 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -image leeopticianslogo_jpg -text Label 
    vTcl:DefineAlias "$top.lab59" "Label6" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent67 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 314 
    vTcl:DefineAlias "$top.ent67" "BranchIDEntry" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab68 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text BranchID 
    vTcl:DefineAlias "$top.lab68" "BranchIDLbl" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab69 \
        -background #ffffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text Total 
    vTcl:DefineAlias "$top.lab69" "PriceLbl" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent70 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) -insertbackground black -width 314 
    vTcl:DefineAlias "$top.ent70" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra46 \
        -in $top -x 0 -relx 0.733 -y 0 -rely 0.237 -width 0 -relwidth 0.208 \
        -height 0 -relheight 0.567 -anchor nw -bordermode ignore 
    place $top.ent47 \
        -in $top -x 0 -relx 0.15 -y 0 -rely 0.265 -width 314 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent48 \
        -in $top -x 0 -relx 0.15 -y 0 -rely 0.377 -width 314 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent49 \
        -in $top -x 0 -relx 0.15 -y 0 -rely 0.433 -width 314 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent50 \
        -in $top -x 0 -relx 0.15 -y 0 -rely 0.489 -width 314 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent51 \
        -in $top -x 0 -relx 0.15 -y 0 -rely 0.545 -width 314 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab53 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.265 -width 0 -relwidth 0.09 \
        -height 0 -relheight 0.029 -anchor nw -bordermode ignore 
    place $top.lab55 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.377 -width 0 -relwidth 0.123 \
        -height 0 -relheight 0.029 -anchor nw -bordermode ignore 
    place $top.lab56 \
        -in $top -x 0 -y 0 -rely 0.433 -width 0 -relwidth 0.15 -height 0 \
        -relheight 0.029 -anchor nw -bordermode ignore 
    place $top.lab57 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.489 -width 0 -relwidth 0.115 \
        -height 0 -relheight 0.029 -anchor nw -bordermode ignore 
    place $top.lab58 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.545 -width 0 -relwidth 0.12 \
        -height 0 -relheight 0.029 -anchor nw -bordermode ignore 
    place $top.lab59 \
        -in $top -x 0 -relx 0.333 -y 0 -rely 0.112 -width 0 -relwidth 0.29 \
        -height 0 -relheight 0.071 -anchor nw -bordermode ignore 
    place $top.ent67 \
        -in $top -x 0 -relx 0.15 -y 0 -rely 0.321 -width 314 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab68 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.321 -width 0 -relwidth 0.107 \
        -height 0 -relheight 0.029 -anchor nw -bordermode ignore 
    place $top.lab69 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.601 -width 0 -relwidth 0.07 \
        -height 0 -relheight 0.029 -anchor nw -bordermode ignore 
    place $top.ent70 \
        -in $top -x 0 -relx 0.15 -y 0 -rely 0.601 -width 314 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

