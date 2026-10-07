Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
---------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.1 (lin64) Build 5076996 Wed May 22 18:36:09 MDT 2024
| Date         : Wed Oct  7 10:02:07 2026
| Host         : LAPTOP-CSM08B9Q running 64-bit Ubuntu 26.04 LTS
| Command      : report_timing_summary -datasheet -max_paths 10 -file digilent_nexys4ddr_timing.rpt
| Design       : digilent_nexys4ddr
| Device       : 7a100t-csg324
| Speed File   : -1  PRODUCTION 1.23 2018-06-13
| Design State : Physopt postRoute
---------------------------------------------------------------------------------------------------------------------------------------------

Timing Summary Report

------------------------------------------------------------------------------------------------
| Timer Settings
| --------------
------------------------------------------------------------------------------------------------

  Enable Multi Corner Analysis               :  Yes
  Enable Pessimism Removal                   :  Yes
  Pessimism Removal Resolution               :  Nearest Common Node
  Enable Input Delay Default Clock           :  No
  Enable Preset / Clear Arcs                 :  No
  Disable Flight Delays                      :  No
  Ignore I/O Paths                           :  No
  Timing Early Launch at Borrowing Latches   :  No
  Borrow Time for Max Delay Exceptions       :  Yes
  Merge Timing Exceptions                    :  Yes
  Inter-SLR Compensation                     :  Conservative

  Corner  Analyze    Analyze    
  Name    Max Paths  Min Paths  
  ------  ---------  ---------  
  Slow    Yes        Yes        
  Fast    Yes        Yes        


------------------------------------------------------------------------------------------------
| Report Methodology
| ------------------
------------------------------------------------------------------------------------------------

No report available as report_methodology has not been run prior. Run report_methodology on the current design for the summary of methodology violations.



check_timing report

Table of Contents
-----------------
1. checking no_clock (0)
2. checking constant_clock (0)
3. checking pulse_width_clock (0)
4. checking unconstrained_internal_endpoints (0)
5. checking no_input_delay (18)
6. checking no_output_delay (60)
7. checking multiple_clock (0)
8. checking generated_clocks (0)
9. checking loops (0)
10. checking partial_input_delay (0)
11. checking partial_output_delay (0)
12. checking latch_loops (0)

1. checking no_clock (0)
------------------------
 There are 0 register/latch pins with no clock.


2. checking constant_clock (0)
------------------------------
 There are 0 register/latch pins with constant_clock.


3. checking pulse_width_clock (0)
---------------------------------
 There are 0 register/latch pins which need pulse_width check


4. checking unconstrained_internal_endpoints (0)
------------------------------------------------
 There are 0 pins that are not constrained for maximum delay.

 There are 0 pins that are not constrained for maximum delay due to constant clock.


5. checking no_input_delay (18)
-------------------------------
 There are 18 input ports with no input delay specified. (HIGH)

 There are 0 input ports with no input delay but user has a false path constraint.


6. checking no_output_delay (60)
--------------------------------
 There are 60 ports with no output delay specified. (HIGH)

 There are 0 ports with no output delay but user has a false path constraint

 There are 0 ports with no output delay but with a timing clock defined on it or propagating through it


7. checking multiple_clock (0)
------------------------------
 There are 0 register/latch pins with multiple clocks.


8. checking generated_clocks (0)
--------------------------------
 There are 0 generated clocks that are not connected to a clock source.


9. checking loops (0)
---------------------
 There are 0 combinational loops in the design.


10. checking partial_input_delay (0)
------------------------------------
 There are 0 input ports with partial input delay specified.


11. checking partial_output_delay (0)
-------------------------------------
 There are 0 ports with partial output delay specified.


12. checking latch_loops (0)
----------------------------
 There are 0 combinational latch loops in the design through latch input



------------------------------------------------------------------------------------------------
| Design Timing Summary
| ---------------------
------------------------------------------------------------------------------------------------

    WNS(ns)      TNS(ns)  TNS Failing Endpoints  TNS Total Endpoints      WHS(ns)      THS(ns)  THS Failing Endpoints  THS Total Endpoints     WPWS(ns)     TPWS(ns)  TPWS Failing Endpoints  TPWS Total Endpoints  
    -------      -------  ---------------------  -------------------      -------      -------  ---------------------  -------------------     --------     --------  ----------------------  --------------------  
      0.962        0.000                      0                13972        0.032        0.000                      0                13972        0.264        0.000                       0                  5034  


All user specified timing constraints are met.


------------------------------------------------------------------------------------------------
| Clock Summary
| -------------
------------------------------------------------------------------------------------------------

Clock                          Waveform(ns)         Period(ns)      Frequency(MHz)
-----                          ------------         ----------      --------------
clk100                         {0.000 5.000}        10.000          100.000         
  soc_builder_basesoc_mmcm_fb  {0.000 5.000}        10.000          100.000         
  soc_crg_clkout0              {0.000 6.667}        13.333          75.000          
  soc_crg_clkout1              {0.000 3.333}        6.667           150.000         
  soc_crg_clkout2              {1.667 5.000}        6.667           150.000         
  soc_crg_clkout3              {0.000 2.500}        5.000           200.000         


------------------------------------------------------------------------------------------------
| Intra Clock Table
| -----------------
------------------------------------------------------------------------------------------------

Clock                              WNS(ns)      TNS(ns)  TNS Failing Endpoints  TNS Total Endpoints      WHS(ns)      THS(ns)  THS Failing Endpoints  THS Total Endpoints     WPWS(ns)     TPWS(ns)  TPWS Failing Endpoints  TPWS Total Endpoints  
-----                              -------      -------  ---------------------  -------------------      -------      -------  ---------------------  -------------------     --------     --------  ----------------------  --------------------  
clk100                               8.230        0.000                      0                    7        0.230        0.000                      0                    7        3.000        0.000                       0                    10  
  soc_builder_basesoc_mmcm_fb                                                                                                                                                    8.751        0.000                       0                     2  
  soc_crg_clkout0                    0.962        0.000                      0                13951        0.032        0.000                      0                13951        5.417        0.000                       0                  4933  
  soc_crg_clkout1                                                                                                                                                                4.511        0.000                       0                    75  
  soc_crg_clkout2                                                                                                                                                                4.511        0.000                       0                     4  
  soc_crg_clkout3                    1.246        0.000                      0                   14        0.122        0.000                      0                   14        0.264        0.000                       0                    10  


------------------------------------------------------------------------------------------------
| Inter Clock Table
| -----------------
------------------------------------------------------------------------------------------------

From Clock    To Clock          WNS(ns)      TNS(ns)  TNS Failing Endpoints  TNS Total Endpoints      WHS(ns)      THS(ns)  THS Failing Endpoints  THS Total Endpoints  
----------    --------          -------      -------  ---------------------  -------------------      -------      -------  ---------------------  -------------------  


------------------------------------------------------------------------------------------------
| Other Path Groups Table
| -----------------------
------------------------------------------------------------------------------------------------

Path Group    From Clock    To Clock          WNS(ns)      TNS(ns)  TNS Failing Endpoints  TNS Total Endpoints      WHS(ns)      THS(ns)  THS Failing Endpoints  THS Total Endpoints  
----------    ----------    --------          -------      -------  ---------------------  -------------------      -------      -------  ---------------------  -------------------  


------------------------------------------------------------------------------------------------
| Timing Details
| --------------
------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------
From Clock:  clk100
  To Clock:  clk100

Setup :            0  Failing Endpoints,  Worst Slack        8.230ns,  Total Violation        0.000ns
Hold  :            0  Failing Endpoints,  Worst Slack        0.230ns,  Total Violation        0.000ns
PW    :            0  Failing Endpoints,  Worst Slack        3.000ns,  Total Violation        0.000ns
---------------------------------------------------------------------------------------------------


Max Delay Paths
--------------------------------------------------------------------------------------
Slack (MET) :             8.230ns  (required time - arrival time)
  Source:                 FDCE_6/C
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Destination:            FDCE_7/D
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Path Group:             clk100
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            10.000ns  (clk100 rise@10.000ns - clk100 rise@0.000ns)
  Data Path Delay:        1.198ns  (logic 0.419ns (34.989%)  route 0.779ns (65.011%))
  Logic Levels:           0  
  Clock Path Skew:        -0.299ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    7.944ns = ( 17.944 - 10.000 ) 
    Source Clock Delay      (SCD):    8.953ns
    Clock Pessimism Removal (CPR):    0.710ns
  Clock Uncertainty:      0.035ns  ((TSJ^2 + TIJ^2)^1/2 + DJ) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Total Input Jitter      (TIJ):    0.000ns
    Discrete Jitter          (DJ):    0.000ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           2.752     8.953    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_6/C
  -------------------------------------------------------------------    -------------------
    SLICE_X73Y102        FDCE (Prop_fdce_C_Q)         0.419     9.372 r  FDCE_6/Q
                         net (fo=1, routed)           0.779    10.151    soc_builder_basesoc_reset6
    SLICE_X64Y102        FDCE                                         r  FDCE_7/D
  -------------------------------------------------------------------    -------------------

                         (clock clk100 rise edge)    10.000    10.000 r  
    E3                                                0.000    10.000 r  clk100 (IN)
                         net (fo=0)                   0.000    10.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411    11.411 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920    13.331    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091    13.422 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    15.636    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    15.736 r  clk100_inst/O
                         net (fo=9, routed)           2.208    17.944    soc_crg_clkin
    SLICE_X64Y102        FDCE                                         r  FDCE_7/C
                         clock pessimism              0.710    18.655    
                         clock uncertainty           -0.035    18.619    
    SLICE_X64Y102        FDCE (Setup_fdce_C_D)       -0.239    18.380    FDCE_7
  -------------------------------------------------------------------
                         required time                         18.380    
                         arrival time                         -10.151    
  -------------------------------------------------------------------
                         slack                                  8.230    

Slack (MET) :             8.515ns  (required time - arrival time)
  Source:                 FDCE/C
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Destination:            FDCE_1/D
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Path Group:             clk100
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            10.000ns  (clk100 rise@10.000ns - clk100 rise@0.000ns)
  Data Path Delay:        1.373ns  (logic 0.456ns (33.213%)  route 0.917ns (66.787%))
  Logic Levels:           0  
  Clock Path Skew:        0.018ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    8.061ns = ( 18.061 - 10.000 ) 
    Source Clock Delay      (SCD):    8.753ns
    Clock Pessimism Removal (CPR):    0.710ns
  Clock Uncertainty:      0.035ns  ((TSJ^2 + TIJ^2)^1/2 + DJ) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Total Input Jitter      (TIJ):    0.000ns
    Discrete Jitter          (DJ):    0.000ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           2.551     8.753    soc_crg_clkin
    SLICE_X73Y92         FDCE                                         r  FDCE/C
  -------------------------------------------------------------------    -------------------
    SLICE_X73Y92         FDCE (Prop_fdce_C_Q)         0.456     9.209 r  FDCE/Q
                         net (fo=1, routed)           0.917    10.126    soc_builder_basesoc_reset0
    SLICE_X73Y102        FDCE                                         r  FDCE_1/D
  -------------------------------------------------------------------    -------------------

                         (clock clk100 rise edge)    10.000    10.000 r  
    E3                                                0.000    10.000 r  clk100 (IN)
                         net (fo=0)                   0.000    10.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411    11.411 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920    13.331    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091    13.422 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    15.636    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    15.736 r  clk100_inst/O
                         net (fo=9, routed)           2.325    18.061    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_1/C
                         clock pessimism              0.710    18.771    
                         clock uncertainty           -0.035    18.736    
    SLICE_X73Y102        FDCE (Setup_fdce_C_D)       -0.095    18.641    FDCE_1
  -------------------------------------------------------------------
                         required time                         18.641    
                         arrival time                         -10.126    
  -------------------------------------------------------------------
                         slack                                  8.515    

Slack (MET) :             8.703ns  (required time - arrival time)
  Source:                 FDCE_1/C
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Destination:            FDCE_2/D
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Path Group:             clk100
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            10.000ns  (clk100 rise@10.000ns - clk100 rise@0.000ns)
  Data Path Delay:        1.169ns  (logic 0.456ns (39.006%)  route 0.713ns (60.994%))
  Logic Levels:           0  
  Clock Path Skew:        0.000ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    8.061ns = ( 18.061 - 10.000 ) 
    Source Clock Delay      (SCD):    8.953ns
    Clock Pessimism Removal (CPR):    0.892ns
  Clock Uncertainty:      0.035ns  ((TSJ^2 + TIJ^2)^1/2 + DJ) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Total Input Jitter      (TIJ):    0.000ns
    Discrete Jitter          (DJ):    0.000ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           2.752     8.953    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_1/C
  -------------------------------------------------------------------    -------------------
    SLICE_X73Y102        FDCE (Prop_fdce_C_Q)         0.456     9.409 r  FDCE_1/Q
                         net (fo=1, routed)           0.713    10.122    soc_builder_basesoc_reset1
    SLICE_X73Y102        FDCE                                         r  FDCE_2/D
  -------------------------------------------------------------------    -------------------

                         (clock clk100 rise edge)    10.000    10.000 r  
    E3                                                0.000    10.000 r  clk100 (IN)
                         net (fo=0)                   0.000    10.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411    11.411 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920    13.331    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091    13.422 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    15.636    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    15.736 r  clk100_inst/O
                         net (fo=9, routed)           2.325    18.061    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_2/C
                         clock pessimism              0.892    18.953    
                         clock uncertainty           -0.035    18.918    
    SLICE_X73Y102        FDCE (Setup_fdce_C_D)       -0.093    18.825    FDCE_2
  -------------------------------------------------------------------
                         required time                         18.825    
                         arrival time                         -10.122    
  -------------------------------------------------------------------
                         slack                                  8.703    

Slack (MET) :             8.837ns  (required time - arrival time)
  Source:                 FDCE_2/C
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Destination:            FDCE_3/D
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Path Group:             clk100
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            10.000ns  (clk100 rise@10.000ns - clk100 rise@0.000ns)
  Data Path Delay:        1.067ns  (logic 0.456ns (42.736%)  route 0.611ns (57.264%))
  Logic Levels:           0  
  Clock Path Skew:        0.000ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    8.061ns = ( 18.061 - 10.000 ) 
    Source Clock Delay      (SCD):    8.953ns
    Clock Pessimism Removal (CPR):    0.892ns
  Clock Uncertainty:      0.035ns  ((TSJ^2 + TIJ^2)^1/2 + DJ) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Total Input Jitter      (TIJ):    0.000ns
    Discrete Jitter          (DJ):    0.000ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           2.752     8.953    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_2/C
  -------------------------------------------------------------------    -------------------
    SLICE_X73Y102        FDCE (Prop_fdce_C_Q)         0.456     9.409 r  FDCE_2/Q
                         net (fo=1, routed)           0.611    10.020    soc_builder_basesoc_reset2
    SLICE_X73Y102        FDCE                                         r  FDCE_3/D
  -------------------------------------------------------------------    -------------------

                         (clock clk100 rise edge)    10.000    10.000 r  
    E3                                                0.000    10.000 r  clk100 (IN)
                         net (fo=0)                   0.000    10.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411    11.411 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920    13.331    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091    13.422 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    15.636    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    15.736 r  clk100_inst/O
                         net (fo=9, routed)           2.325    18.061    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_3/C
                         clock pessimism              0.892    18.953    
                         clock uncertainty           -0.035    18.918    
    SLICE_X73Y102        FDCE (Setup_fdce_C_D)       -0.061    18.857    FDCE_3
  -------------------------------------------------------------------
                         required time                         18.857    
                         arrival time                         -10.020    
  -------------------------------------------------------------------
                         slack                                  8.837    

Slack (MET) :             8.841ns  (required time - arrival time)
  Source:                 FDCE_3/C
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Destination:            FDCE_4/D
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Path Group:             clk100
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            10.000ns  (clk100 rise@10.000ns - clk100 rise@0.000ns)
  Data Path Delay:        1.066ns  (logic 0.456ns (42.776%)  route 0.610ns (57.224%))
  Logic Levels:           0  
  Clock Path Skew:        0.000ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    8.061ns = ( 18.061 - 10.000 ) 
    Source Clock Delay      (SCD):    8.953ns
    Clock Pessimism Removal (CPR):    0.892ns
  Clock Uncertainty:      0.035ns  ((TSJ^2 + TIJ^2)^1/2 + DJ) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Total Input Jitter      (TIJ):    0.000ns
    Discrete Jitter          (DJ):    0.000ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           2.752     8.953    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_3/C
  -------------------------------------------------------------------    -------------------
    SLICE_X73Y102        FDCE (Prop_fdce_C_Q)         0.456     9.409 r  FDCE_3/Q
                         net (fo=1, routed)           0.610    10.019    soc_builder_basesoc_reset3
    SLICE_X73Y102        FDCE                                         r  FDCE_4/D
  -------------------------------------------------------------------    -------------------

                         (clock clk100 rise edge)    10.000    10.000 r  
    E3                                                0.000    10.000 r  clk100 (IN)
                         net (fo=0)                   0.000    10.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411    11.411 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920    13.331    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091    13.422 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    15.636    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    15.736 r  clk100_inst/O
                         net (fo=9, routed)           2.325    18.061    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_4/C
                         clock pessimism              0.892    18.953    
                         clock uncertainty           -0.035    18.918    
    SLICE_X73Y102        FDCE (Setup_fdce_C_D)       -0.058    18.860    FDCE_4
  -------------------------------------------------------------------
                         required time                         18.860    
                         arrival time                         -10.019    
  -------------------------------------------------------------------
                         slack                                  8.841    

Slack (MET) :             8.893ns  (required time - arrival time)
  Source:                 FDCE_4/C
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Destination:            FDCE_5/D
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Path Group:             clk100
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            10.000ns  (clk100 rise@10.000ns - clk100 rise@0.000ns)
  Data Path Delay:        1.024ns  (logic 0.456ns (44.512%)  route 0.568ns (55.488%))
  Logic Levels:           0  
  Clock Path Skew:        0.000ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    8.061ns = ( 18.061 - 10.000 ) 
    Source Clock Delay      (SCD):    8.953ns
    Clock Pessimism Removal (CPR):    0.892ns
  Clock Uncertainty:      0.035ns  ((TSJ^2 + TIJ^2)^1/2 + DJ) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Total Input Jitter      (TIJ):    0.000ns
    Discrete Jitter          (DJ):    0.000ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           2.752     8.953    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_4/C
  -------------------------------------------------------------------    -------------------
    SLICE_X73Y102        FDCE (Prop_fdce_C_Q)         0.456     9.409 r  FDCE_4/Q
                         net (fo=1, routed)           0.568     9.977    soc_builder_basesoc_reset4
    SLICE_X73Y102        FDCE                                         r  FDCE_5/D
  -------------------------------------------------------------------    -------------------

                         (clock clk100 rise edge)    10.000    10.000 r  
    E3                                                0.000    10.000 r  clk100 (IN)
                         net (fo=0)                   0.000    10.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411    11.411 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920    13.331    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091    13.422 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    15.636    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    15.736 r  clk100_inst/O
                         net (fo=9, routed)           2.325    18.061    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_5/C
                         clock pessimism              0.892    18.953    
                         clock uncertainty           -0.035    18.918    
    SLICE_X73Y102        FDCE (Setup_fdce_C_D)       -0.047    18.871    FDCE_5
  -------------------------------------------------------------------
                         required time                         18.871    
                         arrival time                          -9.977    
  -------------------------------------------------------------------
                         slack                                  8.893    

Slack (MET) :             8.926ns  (required time - arrival time)
  Source:                 FDCE_5/C
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Destination:            FDCE_6/D
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Path Group:             clk100
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            10.000ns  (clk100 rise@10.000ns - clk100 rise@0.000ns)
  Data Path Delay:        0.801ns  (logic 0.419ns (52.283%)  route 0.382ns (47.717%))
  Logic Levels:           0  
  Clock Path Skew:        0.000ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    8.061ns = ( 18.061 - 10.000 ) 
    Source Clock Delay      (SCD):    8.953ns
    Clock Pessimism Removal (CPR):    0.892ns
  Clock Uncertainty:      0.035ns  ((TSJ^2 + TIJ^2)^1/2 + DJ) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Total Input Jitter      (TIJ):    0.000ns
    Discrete Jitter          (DJ):    0.000ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           2.752     8.953    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_5/C
  -------------------------------------------------------------------    -------------------
    SLICE_X73Y102        FDCE (Prop_fdce_C_Q)         0.419     9.372 r  FDCE_5/Q
                         net (fo=1, routed)           0.382     9.754    soc_builder_basesoc_reset5
    SLICE_X73Y102        FDCE                                         r  FDCE_6/D
  -------------------------------------------------------------------    -------------------

                         (clock clk100 rise edge)    10.000    10.000 r  
    E3                                                0.000    10.000 r  clk100 (IN)
                         net (fo=0)                   0.000    10.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411    11.411 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920    13.331    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091    13.422 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    15.636    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    15.736 r  clk100_inst/O
                         net (fo=9, routed)           2.325    18.061    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_6/C
                         clock pessimism              0.892    18.953    
                         clock uncertainty           -0.035    18.918    
    SLICE_X73Y102        FDCE (Setup_fdce_C_D)       -0.237    18.681    FDCE_6
  -------------------------------------------------------------------
                         required time                         18.681    
                         arrival time                          -9.754    
  -------------------------------------------------------------------
                         slack                                  8.926    





Min Delay Paths
--------------------------------------------------------------------------------------
Slack (MET) :             0.230ns  (arrival time - required time)
  Source:                 FDCE_5/C
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Destination:            FDCE_6/D
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Path Group:             clk100
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (clk100 rise@0.000ns - clk100 rise@0.000ns)
  Data Path Delay:        0.247ns  (logic 0.128ns (51.736%)  route 0.119ns (48.264%))
  Logic Levels:           0  
  Clock Path Skew:        0.000ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    3.724ns
    Source Clock Delay      (SCD):    2.948ns
    Clock Pessimism Removal (CPR):    0.776ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           1.128     2.948    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_5/C
  -------------------------------------------------------------------    -------------------
    SLICE_X73Y102        FDCE (Prop_fdce_C_Q)         0.128     3.076 r  FDCE_5/Q
                         net (fo=1, routed)           0.119     3.196    soc_builder_basesoc_reset5
    SLICE_X73Y102        FDCE                                         r  FDCE_6/D
  -------------------------------------------------------------------    -------------------

                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.322     3.724    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_6/C
                         clock pessimism             -0.776     2.948    
    SLICE_X73Y102        FDCE (Hold_fdce_C_D)         0.017     2.965    FDCE_6
  -------------------------------------------------------------------
                         required time                         -2.965    
                         arrival time                           3.196    
  -------------------------------------------------------------------
                         slack                                  0.230    

Slack (MET) :             0.242ns  (arrival time - required time)
  Source:                 FDCE_4/C
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Destination:            FDCE_5/D
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Path Group:             clk100
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (clk100 rise@0.000ns - clk100 rise@0.000ns)
  Data Path Delay:        0.317ns  (logic 0.141ns (44.418%)  route 0.176ns (55.581%))
  Logic Levels:           0  
  Clock Path Skew:        0.000ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    3.724ns
    Source Clock Delay      (SCD):    2.948ns
    Clock Pessimism Removal (CPR):    0.776ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           1.128     2.948    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_4/C
  -------------------------------------------------------------------    -------------------
    SLICE_X73Y102        FDCE (Prop_fdce_C_Q)         0.141     3.089 r  FDCE_4/Q
                         net (fo=1, routed)           0.176     3.266    soc_builder_basesoc_reset4
    SLICE_X73Y102        FDCE                                         r  FDCE_5/D
  -------------------------------------------------------------------    -------------------

                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.322     3.724    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_5/C
                         clock pessimism             -0.776     2.948    
    SLICE_X73Y102        FDCE (Hold_fdce_C_D)         0.075     3.023    FDCE_5
  -------------------------------------------------------------------
                         required time                         -3.023    
                         arrival time                           3.266    
  -------------------------------------------------------------------
                         slack                                  0.242    

Slack (MET) :             0.270ns  (arrival time - required time)
  Source:                 FDCE_3/C
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Destination:            FDCE_4/D
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Path Group:             clk100
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (clk100 rise@0.000ns - clk100 rise@0.000ns)
  Data Path Delay:        0.342ns  (logic 0.141ns (41.226%)  route 0.201ns (58.774%))
  Logic Levels:           0  
  Clock Path Skew:        0.000ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    3.724ns
    Source Clock Delay      (SCD):    2.948ns
    Clock Pessimism Removal (CPR):    0.776ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           1.128     2.948    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_3/C
  -------------------------------------------------------------------    -------------------
    SLICE_X73Y102        FDCE (Prop_fdce_C_Q)         0.141     3.089 r  FDCE_3/Q
                         net (fo=1, routed)           0.201     3.290    soc_builder_basesoc_reset3
    SLICE_X73Y102        FDCE                                         r  FDCE_4/D
  -------------------------------------------------------------------    -------------------

                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.322     3.724    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_4/C
                         clock pessimism             -0.776     2.948    
    SLICE_X73Y102        FDCE (Hold_fdce_C_D)         0.072     3.020    FDCE_4
  -------------------------------------------------------------------
                         required time                         -3.020    
                         arrival time                           3.290    
  -------------------------------------------------------------------
                         slack                                  0.270    

Slack (MET) :             0.272ns  (arrival time - required time)
  Source:                 FDCE_2/C
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Destination:            FDCE_3/D
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Path Group:             clk100
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (clk100 rise@0.000ns - clk100 rise@0.000ns)
  Data Path Delay:        0.342ns  (logic 0.141ns (41.226%)  route 0.201ns (58.774%))
  Logic Levels:           0  
  Clock Path Skew:        0.000ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    3.724ns
    Source Clock Delay      (SCD):    2.948ns
    Clock Pessimism Removal (CPR):    0.776ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           1.128     2.948    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_2/C
  -------------------------------------------------------------------    -------------------
    SLICE_X73Y102        FDCE (Prop_fdce_C_Q)         0.141     3.089 r  FDCE_2/Q
                         net (fo=1, routed)           0.201     3.290    soc_builder_basesoc_reset2
    SLICE_X73Y102        FDCE                                         r  FDCE_3/D
  -------------------------------------------------------------------    -------------------

                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.322     3.724    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_3/C
                         clock pessimism             -0.776     2.948    
    SLICE_X73Y102        FDCE (Hold_fdce_C_D)         0.070     3.018    FDCE_3
  -------------------------------------------------------------------
                         required time                         -3.018    
                         arrival time                           3.290    
  -------------------------------------------------------------------
                         slack                                  0.272    

Slack (MET) :             0.283ns  (arrival time - required time)
  Source:                 FDCE/C
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Destination:            FDCE_1/D
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Path Group:             clk100
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (clk100 rise@0.000ns - clk100 rise@0.000ns)
  Data Path Delay:        0.500ns  (logic 0.141ns (28.202%)  route 0.359ns (71.798%))
  Logic Levels:           0  
  Clock Path Skew:        0.170ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    3.724ns
    Source Clock Delay      (SCD):    2.860ns
    Clock Pessimism Removal (CPR):    0.694ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           1.039     2.860    soc_crg_clkin
    SLICE_X73Y92         FDCE                                         r  FDCE/C
  -------------------------------------------------------------------    -------------------
    SLICE_X73Y92         FDCE (Prop_fdce_C_Q)         0.141     3.001 r  FDCE/Q
                         net (fo=1, routed)           0.359     3.360    soc_builder_basesoc_reset0
    SLICE_X73Y102        FDCE                                         r  FDCE_1/D
  -------------------------------------------------------------------    -------------------

                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.322     3.724    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_1/C
                         clock pessimism             -0.694     3.030    
    SLICE_X73Y102        FDCE (Hold_fdce_C_D)         0.046     3.076    FDCE_1
  -------------------------------------------------------------------
                         required time                         -3.076    
                         arrival time                           3.360    
  -------------------------------------------------------------------
                         slack                                  0.283    

Slack (MET) :             0.340ns  (arrival time - required time)
  Source:                 FDCE_1/C
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Destination:            FDCE_2/D
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Path Group:             clk100
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (clk100 rise@0.000ns - clk100 rise@0.000ns)
  Data Path Delay:        0.387ns  (logic 0.141ns (36.428%)  route 0.246ns (63.572%))
  Logic Levels:           0  
  Clock Path Skew:        0.000ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    3.724ns
    Source Clock Delay      (SCD):    2.948ns
    Clock Pessimism Removal (CPR):    0.776ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           1.128     2.948    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_1/C
  -------------------------------------------------------------------    -------------------
    SLICE_X73Y102        FDCE (Prop_fdce_C_Q)         0.141     3.089 r  FDCE_1/Q
                         net (fo=1, routed)           0.246     3.335    soc_builder_basesoc_reset1
    SLICE_X73Y102        FDCE                                         r  FDCE_2/D
  -------------------------------------------------------------------    -------------------

                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.322     3.724    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_2/C
                         clock pessimism             -0.776     2.948    
    SLICE_X73Y102        FDCE (Hold_fdce_C_D)         0.047     2.995    FDCE_2
  -------------------------------------------------------------------
                         required time                         -2.995    
                         arrival time                           3.335    
  -------------------------------------------------------------------
                         slack                                  0.340    

Slack (MET) :             0.445ns  (arrival time - required time)
  Source:                 FDCE_6/C
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Destination:            FDCE_7/D
                            (rising edge-triggered cell FDCE clocked by clk100  {rise@0.000ns fall@5.000ns period=10.000ns})
  Path Group:             clk100
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (clk100 rise@0.000ns - clk100 rise@0.000ns)
  Data Path Delay:        0.447ns  (logic 0.128ns (28.667%)  route 0.319ns (71.333%))
  Logic Levels:           0  
  Clock Path Skew:        -0.016ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    3.627ns
    Source Clock Delay      (SCD):    2.948ns
    Clock Pessimism Removal (CPR):    0.694ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           1.128     2.948    soc_crg_clkin
    SLICE_X73Y102        FDCE                                         r  FDCE_6/C
  -------------------------------------------------------------------    -------------------
    SLICE_X73Y102        FDCE (Prop_fdce_C_Q)         0.128     3.076 r  FDCE_6/Q
                         net (fo=1, routed)           0.319     3.395    soc_builder_basesoc_reset6
    SLICE_X64Y102        FDCE                                         r  FDCE_7/D
  -------------------------------------------------------------------    -------------------

                         (clock clk100 rise edge)     0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.224     3.627    soc_crg_clkin
    SLICE_X64Y102        FDCE                                         r  FDCE_7/C
                         clock pessimism             -0.694     2.933    
    SLICE_X64Y102        FDCE (Hold_fdce_C_D)         0.017     2.950    FDCE_7
  -------------------------------------------------------------------
                         required time                         -2.950    
                         arrival time                           3.395    
  -------------------------------------------------------------------
                         slack                                  0.445    





Pulse Width Checks
--------------------------------------------------------------------------------------
Clock Name:         clk100
Waveform(ns):       { 0.000 5.000 }
Period(ns):         10.000
Sources:            { clk100 }

Check Type        Corner  Lib Pin            Reference Pin  Required(ns)  Actual(ns)  Slack(ns)  Location         Pin
Min Period        n/a     BUFG/I             n/a            2.155         10.000      7.845      BUFGCTRL_X0Y16   clk100_IBUF_BUFG_inst/I
Min Period        n/a     MMCME2_ADV/CLKIN1  n/a            1.249         10.000      8.751      MMCME2_ADV_X0Y0  MMCME2_ADV/CLKIN1
Min Period        n/a     FDCE/C             n/a            1.000         10.000      9.000      SLICE_X73Y92     FDCE/C
Min Period        n/a     FDCE/C             n/a            1.000         10.000      9.000      SLICE_X73Y102    FDCE_1/C
Min Period        n/a     FDCE/C             n/a            1.000         10.000      9.000      SLICE_X73Y102    FDCE_2/C
Min Period        n/a     FDCE/C             n/a            1.000         10.000      9.000      SLICE_X73Y102    FDCE_3/C
Min Period        n/a     FDCE/C             n/a            1.000         10.000      9.000      SLICE_X73Y102    FDCE_4/C
Min Period        n/a     FDCE/C             n/a            1.000         10.000      9.000      SLICE_X73Y102    FDCE_5/C
Min Period        n/a     FDCE/C             n/a            1.000         10.000      9.000      SLICE_X73Y102    FDCE_6/C
Min Period        n/a     FDCE/C             n/a            1.000         10.000      9.000      SLICE_X64Y102    FDCE_7/C
Max Period        n/a     MMCME2_ADV/CLKIN1  n/a            100.000       10.000      90.000     MMCME2_ADV_X0Y0  MMCME2_ADV/CLKIN1
Low Pulse Width   Slow    MMCME2_ADV/CLKIN1  n/a            2.000         5.000       3.000      MMCME2_ADV_X0Y0  MMCME2_ADV/CLKIN1
Low Pulse Width   Fast    MMCME2_ADV/CLKIN1  n/a            2.000         5.000       3.000      MMCME2_ADV_X0Y0  MMCME2_ADV/CLKIN1
Low Pulse Width   Slow    FDCE/C             n/a            0.500         5.000       4.500      SLICE_X73Y92     FDCE/C
Low Pulse Width   Fast    FDCE/C             n/a            0.500         5.000       4.500      SLICE_X73Y92     FDCE/C
Low Pulse Width   Slow    FDCE/C             n/a            0.500         5.000       4.500      SLICE_X73Y102    FDCE_1/C
Low Pulse Width   Fast    FDCE/C             n/a            0.500         5.000       4.500      SLICE_X73Y102    FDCE_1/C
Low Pulse Width   Slow    FDCE/C             n/a            0.500         5.000       4.500      SLICE_X73Y102    FDCE_2/C
Low Pulse Width   Fast    FDCE/C             n/a            0.500         5.000       4.500      SLICE_X73Y102    FDCE_2/C
Low Pulse Width   Slow    FDCE/C             n/a            0.500         5.000       4.500      SLICE_X73Y102    FDCE_3/C
Low Pulse Width   Fast    FDCE/C             n/a            0.500         5.000       4.500      SLICE_X73Y102    FDCE_3/C
High Pulse Width  Slow    MMCME2_ADV/CLKIN1  n/a            2.000         5.000       3.000      MMCME2_ADV_X0Y0  MMCME2_ADV/CLKIN1
High Pulse Width  Fast    MMCME2_ADV/CLKIN1  n/a            2.000         5.000       3.000      MMCME2_ADV_X0Y0  MMCME2_ADV/CLKIN1
High Pulse Width  Slow    FDCE/C             n/a            0.500         5.000       4.500      SLICE_X73Y92     FDCE/C
High Pulse Width  Fast    FDCE/C             n/a            0.500         5.000       4.500      SLICE_X73Y92     FDCE/C
High Pulse Width  Slow    FDCE/C             n/a            0.500         5.000       4.500      SLICE_X73Y102    FDCE_1/C
High Pulse Width  Fast    FDCE/C             n/a            0.500         5.000       4.500      SLICE_X73Y102    FDCE_1/C
High Pulse Width  Slow    FDCE/C             n/a            0.500         5.000       4.500      SLICE_X73Y102    FDCE_2/C
High Pulse Width  Fast    FDCE/C             n/a            0.500         5.000       4.500      SLICE_X73Y102    FDCE_2/C
High Pulse Width  Slow    FDCE/C             n/a            0.500         5.000       4.500      SLICE_X73Y102    FDCE_3/C
High Pulse Width  Fast    FDCE/C             n/a            0.500         5.000       4.500      SLICE_X73Y102    FDCE_3/C



---------------------------------------------------------------------------------------------------
From Clock:  soc_builder_basesoc_mmcm_fb
  To Clock:  soc_builder_basesoc_mmcm_fb

Setup :           NA  Failing Endpoints,  Worst Slack           NA  ,  Total Violation           NA
Hold  :           NA  Failing Endpoints,  Worst Slack           NA  ,  Total Violation           NA
PW    :            0  Failing Endpoints,  Worst Slack        8.751ns,  Total Violation        0.000ns
---------------------------------------------------------------------------------------------------


Pulse Width Checks
--------------------------------------------------------------------------------------
Clock Name:         soc_builder_basesoc_mmcm_fb
Waveform(ns):       { 0.000 5.000 }
Period(ns):         10.000
Sources:            { MMCME2_ADV/CLKFBOUT }

Check Type  Corner  Lib Pin              Reference Pin  Required(ns)  Actual(ns)  Slack(ns)  Location         Pin
Min Period  n/a     MMCME2_ADV/CLKFBOUT  n/a            1.249         10.000      8.751      MMCME2_ADV_X0Y0  MMCME2_ADV/CLKFBOUT
Min Period  n/a     MMCME2_ADV/CLKFBIN   n/a            1.249         10.000      8.751      MMCME2_ADV_X0Y0  MMCME2_ADV/CLKFBIN
Max Period  n/a     MMCME2_ADV/CLKFBIN   n/a            100.000       10.000      90.000     MMCME2_ADV_X0Y0  MMCME2_ADV/CLKFBIN
Max Period  n/a     MMCME2_ADV/CLKFBOUT  n/a            213.360       10.000      203.360    MMCME2_ADV_X0Y0  MMCME2_ADV/CLKFBOUT



---------------------------------------------------------------------------------------------------
From Clock:  soc_crg_clkout0
  To Clock:  soc_crg_clkout0

Setup :            0  Failing Endpoints,  Worst Slack        0.962ns,  Total Violation        0.000ns
Hold  :            0  Failing Endpoints,  Worst Slack        0.032ns,  Total Violation        0.000ns
PW    :            0  Failing Endpoints,  Worst Slack        5.417ns,  Total Violation        0.000ns
---------------------------------------------------------------------------------------------------


Max Delay Paths
--------------------------------------------------------------------------------------
Slack (MET) :             0.962ns  (required time - arrival time)
  Source:                 VexRiscv/decode_to_execute_RS2_reg[0]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            VexRiscv/IBusCachedPlugin_cache/banks_0_reg/ADDRBWRADDR[10]
                            (rising edge-triggered cell RAMB36E1 clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            13.333ns  (soc_crg_clkout0 rise@13.333ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        11.766ns  (logic 3.483ns (29.603%)  route 8.283ns (70.397%))
  Logic Levels:           16  (CARRY4=8 LUT4=1 LUT5=3 LUT6=4)
  Clock Path Skew:        0.030ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    11.114ns = ( 24.447 - 13.333 ) 
    Source Clock Delay      (SCD):    11.933ns
    Clock Pessimism Removal (CPR):    0.850ns
  Clock Uncertainty:      0.070ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.121ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG/O
                         net (fo=4933, routed)        1.613    11.933    VexRiscv/stageB_flusher_counter_reg[0]
    SLICE_X51Y72         FDRE                                         r  VexRiscv/decode_to_execute_RS2_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X51Y72         FDRE (Prop_fdre_C_Q)         0.456    12.389 f  VexRiscv/decode_to_execute_RS2_reg[0]/Q
                         net (fo=10, routed)          1.185    13.574    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[31]_i_3[0]
    SLICE_X63Y72         LUT5 (Prop_lut5_I1_O)        0.124    13.698 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_SHIFT_RIGHT[31]_i_5/O
                         net (fo=35, routed)          0.802    14.500    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19_0
    SLICE_X60Y75         LUT6 (Prop_lut6_I4_O)        0.124    14.624 r  VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_26/O
                         net (fo=1, routed)           0.622    15.246    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_26_n_0
    SLICE_X61Y75         CARRY4 (Prop_carry4_S[0]_CO[3])
                                                      0.656    15.902 r  VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19/CO[3]
                         net (fo=1, routed)           0.000    15.902    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19_n_0
    SLICE_X61Y76         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.016 r  VexRiscv/dataCache_1/ways_0_tags_reg_i_21/CO[3]
                         net (fo=1, routed)           0.000    16.016    VexRiscv/dataCache_1/ways_0_tags_reg_i_21_n_0
    SLICE_X61Y77         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.130 r  VexRiscv/dataCache_1/ways_0_tags_reg_i_20/CO[3]
                         net (fo=1, routed)           0.000    16.130    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[12]_i_2[0]
    SLICE_X61Y78         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.244 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[15]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.244    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[15]_i_4_n_0
    SLICE_X61Y79         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.358 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[19]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.358    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[19]_i_4_n_0
    SLICE_X61Y80         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.472 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[23]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.472    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[23]_i_4_n_0
    SLICE_X61Y81         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.586 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[27]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.586    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[27]_i_4_n_0
    SLICE_X61Y82         CARRY4 (Prop_carry4_CI_O[3])
                                                      0.313    16.899 f  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[31]_i_5/O[3]
                         net (fo=2, routed)           0.763    17.662    VexRiscv/IBusCachedPlugin_cache/_zz_execute_SrcPlugin_addSub[19]
    SLICE_X62Y77         LUT5 (Prop_lut5_I1_O)        0.306    17.968 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[0]_i_7/O
                         net (fo=2, routed)           0.464    18.432    VexRiscv/IBusCachedPlugin_cache/decode_to_execute_SRC2_FORCE_ZERO_reg
    SLICE_X62Y77         LUT6 (Prop_lut6_I1_O)        0.124    18.556 r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_58/O
                         net (fo=1, routed)           0.707    19.263    VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_58_n_0
    SLICE_X67Y71         LUT5 (Prop_lut5_I1_O)        0.124    19.387 f  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_35/O
                         net (fo=6, routed)           1.046    20.434    VexRiscv/IBusCachedPlugin_cache/decode_to_execute_BRANCH_CTRL_reg[1]
    SLICE_X78Y68         LUT4 (Prop_lut4_I1_O)        0.117    20.551 r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_39/O
                         net (fo=30, routed)          1.078    21.628    VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_39_n_0
    SLICE_X69Y71         LUT6 (Prop_lut6_I2_O)        0.331    21.959 f  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_21/O
                         net (fo=2, routed)           0.587    22.547    VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_21_n_0
    SLICE_X70Y68         LUT6 (Prop_lut6_I5_O)        0.124    22.671 r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_6/O
                         net (fo=2, routed)           1.028    23.699    VexRiscv/IBusCachedPlugin_cache/IBusCachedPlugin_iBusRsp_stages_0_input_payload[7]
    RAMB36_X3Y13         RAMB36E1                                     r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg/ADDRBWRADDR[10]
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                     13.333    13.333 r  
    E3                                                0.000    13.333 r  clk100 (IN)
                         net (fo=0)                   0.000    13.333    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411    14.745 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920    16.665    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091    16.756 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    18.969    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    19.069 r  clk100_inst/O
                         net (fo=9, routed)           1.645    20.714    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.083    20.797 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           1.923    22.721    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.091    22.812 r  BUFG/O
                         net (fo=4933, routed)        1.636    24.447    VexRiscv/IBusCachedPlugin_cache/ways_0_tags_reg_0
    RAMB36_X3Y13         RAMB36E1                                     r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg/CLKBWRCLK
                         clock pessimism              0.850    25.297    
                         clock uncertainty           -0.070    25.227    
    RAMB36_X3Y13         RAMB36E1 (Setup_ramb36e1_CLKBWRCLK_ADDRBWRADDR[10])
                                                     -0.566    24.661    VexRiscv/IBusCachedPlugin_cache/banks_0_reg
  -------------------------------------------------------------------
                         required time                         24.661    
                         arrival time                         -23.699    
  -------------------------------------------------------------------
                         slack                                  0.962    

Slack (MET) :             1.002ns  (required time - arrival time)
  Source:                 VexRiscv/decode_to_execute_RS2_reg[0]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            VexRiscv/IBusCachedPlugin_cache/banks_0_reg/ADDRBWRADDR[11]
                            (rising edge-triggered cell RAMB36E1 clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            13.333ns  (soc_crg_clkout0 rise@13.333ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        11.725ns  (logic 3.483ns (29.705%)  route 8.242ns (70.295%))
  Logic Levels:           16  (CARRY4=8 LUT4=1 LUT5=3 LUT6=4)
  Clock Path Skew:        0.030ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    11.114ns = ( 24.447 - 13.333 ) 
    Source Clock Delay      (SCD):    11.933ns
    Clock Pessimism Removal (CPR):    0.850ns
  Clock Uncertainty:      0.070ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.121ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG/O
                         net (fo=4933, routed)        1.613    11.933    VexRiscv/stageB_flusher_counter_reg[0]
    SLICE_X51Y72         FDRE                                         r  VexRiscv/decode_to_execute_RS2_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X51Y72         FDRE (Prop_fdre_C_Q)         0.456    12.389 f  VexRiscv/decode_to_execute_RS2_reg[0]/Q
                         net (fo=10, routed)          1.185    13.574    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[31]_i_3[0]
    SLICE_X63Y72         LUT5 (Prop_lut5_I1_O)        0.124    13.698 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_SHIFT_RIGHT[31]_i_5/O
                         net (fo=35, routed)          0.802    14.500    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19_0
    SLICE_X60Y75         LUT6 (Prop_lut6_I4_O)        0.124    14.624 r  VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_26/O
                         net (fo=1, routed)           0.622    15.246    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_26_n_0
    SLICE_X61Y75         CARRY4 (Prop_carry4_S[0]_CO[3])
                                                      0.656    15.902 r  VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19/CO[3]
                         net (fo=1, routed)           0.000    15.902    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19_n_0
    SLICE_X61Y76         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.016 r  VexRiscv/dataCache_1/ways_0_tags_reg_i_21/CO[3]
                         net (fo=1, routed)           0.000    16.016    VexRiscv/dataCache_1/ways_0_tags_reg_i_21_n_0
    SLICE_X61Y77         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.130 r  VexRiscv/dataCache_1/ways_0_tags_reg_i_20/CO[3]
                         net (fo=1, routed)           0.000    16.130    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[12]_i_2[0]
    SLICE_X61Y78         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.244 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[15]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.244    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[15]_i_4_n_0
    SLICE_X61Y79         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.358 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[19]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.358    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[19]_i_4_n_0
    SLICE_X61Y80         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.472 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[23]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.472    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[23]_i_4_n_0
    SLICE_X61Y81         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.586 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[27]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.586    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[27]_i_4_n_0
    SLICE_X61Y82         CARRY4 (Prop_carry4_CI_O[3])
                                                      0.313    16.899 f  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[31]_i_5/O[3]
                         net (fo=2, routed)           0.763    17.662    VexRiscv/IBusCachedPlugin_cache/_zz_execute_SrcPlugin_addSub[19]
    SLICE_X62Y77         LUT5 (Prop_lut5_I1_O)        0.306    17.968 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[0]_i_7/O
                         net (fo=2, routed)           0.464    18.432    VexRiscv/IBusCachedPlugin_cache/decode_to_execute_SRC2_FORCE_ZERO_reg
    SLICE_X62Y77         LUT6 (Prop_lut6_I1_O)        0.124    18.556 r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_58/O
                         net (fo=1, routed)           0.707    19.263    VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_58_n_0
    SLICE_X67Y71         LUT5 (Prop_lut5_I1_O)        0.124    19.387 f  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_35/O
                         net (fo=6, routed)           1.046    20.434    VexRiscv/IBusCachedPlugin_cache/decode_to_execute_BRANCH_CTRL_reg[1]
    SLICE_X78Y68         LUT4 (Prop_lut4_I1_O)        0.117    20.551 r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_39/O
                         net (fo=30, routed)          0.960    21.511    VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_39_n_0
    SLICE_X69Y70         LUT6 (Prop_lut6_I2_O)        0.331    21.842 f  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_20/O
                         net (fo=2, routed)           0.583    22.425    VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_20_n_0
    SLICE_X70Y68         LUT6 (Prop_lut6_I5_O)        0.124    22.549 r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_5/O
                         net (fo=2, routed)           1.110    23.659    VexRiscv/IBusCachedPlugin_cache/IBusCachedPlugin_iBusRsp_stages_0_input_payload[8]
    RAMB36_X3Y13         RAMB36E1                                     r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg/ADDRBWRADDR[11]
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                     13.333    13.333 r  
    E3                                                0.000    13.333 r  clk100 (IN)
                         net (fo=0)                   0.000    13.333    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411    14.745 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920    16.665    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091    16.756 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    18.969    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    19.069 r  clk100_inst/O
                         net (fo=9, routed)           1.645    20.714    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.083    20.797 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           1.923    22.721    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.091    22.812 r  BUFG/O
                         net (fo=4933, routed)        1.636    24.447    VexRiscv/IBusCachedPlugin_cache/ways_0_tags_reg_0
    RAMB36_X3Y13         RAMB36E1                                     r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg/CLKBWRCLK
                         clock pessimism              0.850    25.297    
                         clock uncertainty           -0.070    25.227    
    RAMB36_X3Y13         RAMB36E1 (Setup_ramb36e1_CLKBWRCLK_ADDRBWRADDR[11])
                                                     -0.566    24.661    VexRiscv/IBusCachedPlugin_cache/banks_0_reg
  -------------------------------------------------------------------
                         required time                         24.661    
                         arrival time                         -23.659    
  -------------------------------------------------------------------
                         slack                                  1.002    

Slack (MET) :             1.022ns  (required time - arrival time)
  Source:                 VexRiscv/decode_to_execute_INSTRUCTION_reg[13]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            VexRiscv/CsrPlugin_minstret_reg[43]/D
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            13.333ns  (soc_crg_clkout0 rise@13.333ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        12.029ns  (logic 2.922ns (24.292%)  route 9.107ns (75.708%))
  Logic Levels:           12  (LUT3=3 LUT5=2 LUT6=6 MUXF7=1)
  Clock Path Skew:        0.049ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    11.066ns = ( 24.399 - 13.333 ) 
    Source Clock Delay      (SCD):    11.938ns
    Clock Pessimism Removal (CPR):    0.922ns
  Clock Uncertainty:      0.070ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.121ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG/O
                         net (fo=4933, routed)        1.618    11.938    VexRiscv/stageB_flusher_counter_reg[0]
    SLICE_X63Y69         FDRE                                         r  VexRiscv/decode_to_execute_INSTRUCTION_reg[13]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X63Y69         FDRE (Prop_fdre_C_Q)         0.456    12.394 f  VexRiscv/decode_to_execute_INSTRUCTION_reg[13]/Q
                         net (fo=182, routed)         0.981    13.375    VexRiscv/CfuPlugin_bus_cmd_payload_function_id[1]
    SLICE_X61Y69         LUT3 (Prop_lut3_I1_O)        0.152    13.527 f  VexRiscv/captured[6]_i_3/O
                         net (fo=4, routed)           0.631    14.159    VexRiscv/decode_to_execute_INSTRUCTION_reg[14]_0
    SLICE_X61Y68         LUT6 (Prop_lut6_I5_O)        0.326    14.485 r  VexRiscv/captured[6]_i_1/O
                         net (fo=220, routed)         0.916    15.400    VexRiscv/$signal$2
    SLICE_X64Y67         LUT3 (Prop_lut3_I1_O)        0.150    15.550 f  VexRiscv/was_updated_i_3/O
                         net (fo=10, routed)          1.035    16.585    VexRiscv/Cfu/fn0/f7buf/$1[2]
    SLICE_X63Y65         LUT5 (Prop_lut5_I4_O)        0.352    16.937 r  VexRiscv/waiting_i_3/O
                         net (fo=4, routed)           0.454    17.391    VexRiscv/dataCache_1/stageA_mask[3]_i_12_0
    SLICE_X62Y65         LUT6 (Prop_lut6_I3_O)        0.326    17.717 r  VexRiscv/dataCache_1/stageA_mask[3]_i_19/O
                         net (fo=1, routed)           0.635    18.352    VexRiscv/dataCache_1/stageA_mask[3]_i_19_n_0
    SLICE_X61Y66         LUT6 (Prop_lut6_I5_O)        0.124    18.476 r  VexRiscv/dataCache_1/stageA_mask[3]_i_12/O
                         net (fo=1, routed)           0.000    18.476    VexRiscv/dataCache_1/stageA_mask[3]_i_12_n_0
    SLICE_X61Y66         MUXF7 (Prop_muxf7_I1_O)      0.217    18.693 r  VexRiscv/dataCache_1/stageA_mask_reg[3]_i_7/O
                         net (fo=3, routed)           0.610    19.302    VexRiscv/dataCache_1/decode_to_execute_INSTRUCTION_reg[30]
    SLICE_X60Y67         LUT6 (Prop_lut6_I0_O)        0.299    19.601 r  VexRiscv/dataCache_1/stageA_mask[3]_i_3/O
                         net (fo=1, routed)           0.282    19.883    VexRiscv/dataCache_1/soc_basesoc_vexriscv_cfu_bus_rsp_valid
    SLICE_X59Y67         LUT6 (Prop_lut6_I2_O)        0.124    20.007 r  VexRiscv/dataCache_1/stageA_mask[3]_i_1/O
                         net (fo=264, routed)         0.563    20.570    VexRiscv/dataCache_1/memory_DivPlugin_div_counter_willClear
    SLICE_X61Y68         LUT6 (Prop_lut6_I3_O)        0.124    20.694 r  VexRiscv/dataCache_1/decode_to_execute_ENV_CTRL[1]_i_1/O
                         net (fo=216, routed)         1.283    21.977    VexRiscv/dataCache_1/when_CsrPlugin_l922_1
    SLICE_X80Y75         LUT5 (Prop_lut5_I1_O)        0.124    22.101 r  VexRiscv/dataCache_1/CsrPlugin_minstret[63]_i_4/O
                         net (fo=32, routed)          1.113    23.215    VexRiscv/dataCache_1/CsrPlugin_minstret[63]_i_4_n_0
    SLICE_X80Y81         LUT3 (Prop_lut3_I1_O)        0.148    23.363 r  VexRiscv/dataCache_1/CsrPlugin_minstret[43]_i_1/O
                         net (fo=1, routed)           0.604    23.967    VexRiscv/p_3_out[43]
    SLICE_X78Y81         FDRE                                         r  VexRiscv/CsrPlugin_minstret_reg[43]/D
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                     13.333    13.333 r  
    E3                                                0.000    13.333 r  clk100 (IN)
                         net (fo=0)                   0.000    13.333    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411    14.745 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920    16.665    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091    16.756 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    18.969    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    19.069 r  clk100_inst/O
                         net (fo=9, routed)           1.645    20.714    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.083    20.797 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           1.923    22.721    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.091    22.812 r  BUFG/O
                         net (fo=4933, routed)        1.587    24.399    VexRiscv/stageB_flusher_counter_reg[0]
    SLICE_X78Y81         FDRE                                         r  VexRiscv/CsrPlugin_minstret_reg[43]/C
                         clock pessimism              0.922    25.321    
                         clock uncertainty           -0.070    25.251    
    SLICE_X78Y81         FDRE (Setup_fdre_C_D)       -0.262    24.989    VexRiscv/CsrPlugin_minstret_reg[43]
  -------------------------------------------------------------------
                         required time                         24.989    
                         arrival time                         -23.967    
  -------------------------------------------------------------------
                         slack                                  1.022    

Slack (MET) :             1.069ns  (required time - arrival time)
  Source:                 VexRiscv/decode_to_execute_RS2_reg[0]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[25]/CE
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            13.333ns  (soc_crg_clkout0 rise@13.333ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        11.879ns  (logic 3.283ns (27.637%)  route 8.596ns (72.363%))
  Logic Levels:           16  (CARRY4=8 LUT2=2 LUT3=1 LUT5=3 LUT6=2)
  Clock Path Skew:        -0.111ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    10.973ns = ( 24.306 - 13.333 ) 
    Source Clock Delay      (SCD):    11.933ns
    Clock Pessimism Removal (CPR):    0.850ns
  Clock Uncertainty:      0.070ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.121ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG/O
                         net (fo=4933, routed)        1.613    11.933    VexRiscv/stageB_flusher_counter_reg[0]
    SLICE_X51Y72         FDRE                                         r  VexRiscv/decode_to_execute_RS2_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X51Y72         FDRE (Prop_fdre_C_Q)         0.456    12.389 f  VexRiscv/decode_to_execute_RS2_reg[0]/Q
                         net (fo=10, routed)          1.185    13.574    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[31]_i_3[0]
    SLICE_X63Y72         LUT5 (Prop_lut5_I1_O)        0.124    13.698 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_SHIFT_RIGHT[31]_i_5/O
                         net (fo=35, routed)          0.802    14.500    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19_0
    SLICE_X60Y75         LUT6 (Prop_lut6_I4_O)        0.124    14.624 r  VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_26/O
                         net (fo=1, routed)           0.622    15.246    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_26_n_0
    SLICE_X61Y75         CARRY4 (Prop_carry4_S[0]_CO[3])
                                                      0.656    15.902 r  VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19/CO[3]
                         net (fo=1, routed)           0.000    15.902    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19_n_0
    SLICE_X61Y76         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.016 r  VexRiscv/dataCache_1/ways_0_tags_reg_i_21/CO[3]
                         net (fo=1, routed)           0.000    16.016    VexRiscv/dataCache_1/ways_0_tags_reg_i_21_n_0
    SLICE_X61Y77         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.130 r  VexRiscv/dataCache_1/ways_0_tags_reg_i_20/CO[3]
                         net (fo=1, routed)           0.000    16.130    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[12]_i_2[0]
    SLICE_X61Y78         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.244 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[15]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.244    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[15]_i_4_n_0
    SLICE_X61Y79         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.358 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[19]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.358    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[19]_i_4_n_0
    SLICE_X61Y80         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.472 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[23]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.472    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[23]_i_4_n_0
    SLICE_X61Y81         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.586 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[27]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.586    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[27]_i_4_n_0
    SLICE_X61Y82         CARRY4 (Prop_carry4_CI_O[3])
                                                      0.313    16.899 f  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[31]_i_5/O[3]
                         net (fo=2, routed)           0.763    17.662    VexRiscv/IBusCachedPlugin_cache/_zz_execute_SrcPlugin_addSub[19]
    SLICE_X62Y77         LUT5 (Prop_lut5_I1_O)        0.306    17.968 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[0]_i_7/O
                         net (fo=2, routed)           0.464    18.432    VexRiscv/IBusCachedPlugin_cache/decode_to_execute_SRC2_FORCE_ZERO_reg
    SLICE_X62Y77         LUT6 (Prop_lut6_I1_O)        0.124    18.556 r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_58/O
                         net (fo=1, routed)           0.707    19.263    VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_58_n_0
    SLICE_X67Y71         LUT5 (Prop_lut5_I1_O)        0.124    19.387 f  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_35/O
                         net (fo=6, routed)           1.050    20.438    VexRiscv/IBusCachedPlugin_cache_n_229
    SLICE_X78Y69         LUT2 (Prop_lut2_I1_O)        0.124    20.562 r  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[1]_i_3/O
                         net (fo=35, routed)          0.900    21.462    VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[1]_i_3_n_0
    SLICE_X84Y69         LUT2 (Prop_lut2_I1_O)        0.124    21.586 f  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[31]_i_5/O
                         net (fo=43, routed)          0.556    22.142    VexRiscv/IBusCachedPlugin_cache/CsrPlugin_exceptionPortCtrl_exceptionContext_code_reg[0]_0
    SLICE_X85Y69         LUT3 (Prop_lut3_I2_O)        0.124    22.266 r  VexRiscv/IBusCachedPlugin_cache/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[31]_i_1/O
                         net (fo=36, routed)          1.546    23.812    VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr
    SLICE_X68Y76         FDRE                                         r  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[25]/CE
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                     13.333    13.333 r  
    E3                                                0.000    13.333 r  clk100 (IN)
                         net (fo=0)                   0.000    13.333    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411    14.745 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920    16.665    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091    16.756 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    18.969    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    19.069 r  clk100_inst/O
                         net (fo=9, routed)           1.645    20.714    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.083    20.797 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           1.923    22.721    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.091    22.812 r  BUFG/O
                         net (fo=4933, routed)        1.494    24.306    VexRiscv/stageB_flusher_counter_reg[0]
    SLICE_X68Y76         FDRE                                         r  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[25]/C
                         clock pessimism              0.850    25.156    
                         clock uncertainty           -0.070    25.086    
    SLICE_X68Y76         FDRE (Setup_fdre_C_CE)      -0.205    24.881    VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[25]
  -------------------------------------------------------------------
                         required time                         24.881    
                         arrival time                         -23.812    
  -------------------------------------------------------------------
                         slack                                  1.069    

Slack (MET) :             1.069ns  (required time - arrival time)
  Source:                 VexRiscv/decode_to_execute_RS2_reg[0]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[28]/CE
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            13.333ns  (soc_crg_clkout0 rise@13.333ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        11.879ns  (logic 3.283ns (27.637%)  route 8.596ns (72.363%))
  Logic Levels:           16  (CARRY4=8 LUT2=2 LUT3=1 LUT5=3 LUT6=2)
  Clock Path Skew:        -0.111ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    10.973ns = ( 24.306 - 13.333 ) 
    Source Clock Delay      (SCD):    11.933ns
    Clock Pessimism Removal (CPR):    0.850ns
  Clock Uncertainty:      0.070ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.121ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG/O
                         net (fo=4933, routed)        1.613    11.933    VexRiscv/stageB_flusher_counter_reg[0]
    SLICE_X51Y72         FDRE                                         r  VexRiscv/decode_to_execute_RS2_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X51Y72         FDRE (Prop_fdre_C_Q)         0.456    12.389 f  VexRiscv/decode_to_execute_RS2_reg[0]/Q
                         net (fo=10, routed)          1.185    13.574    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[31]_i_3[0]
    SLICE_X63Y72         LUT5 (Prop_lut5_I1_O)        0.124    13.698 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_SHIFT_RIGHT[31]_i_5/O
                         net (fo=35, routed)          0.802    14.500    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19_0
    SLICE_X60Y75         LUT6 (Prop_lut6_I4_O)        0.124    14.624 r  VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_26/O
                         net (fo=1, routed)           0.622    15.246    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_26_n_0
    SLICE_X61Y75         CARRY4 (Prop_carry4_S[0]_CO[3])
                                                      0.656    15.902 r  VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19/CO[3]
                         net (fo=1, routed)           0.000    15.902    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19_n_0
    SLICE_X61Y76         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.016 r  VexRiscv/dataCache_1/ways_0_tags_reg_i_21/CO[3]
                         net (fo=1, routed)           0.000    16.016    VexRiscv/dataCache_1/ways_0_tags_reg_i_21_n_0
    SLICE_X61Y77         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.130 r  VexRiscv/dataCache_1/ways_0_tags_reg_i_20/CO[3]
                         net (fo=1, routed)           0.000    16.130    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[12]_i_2[0]
    SLICE_X61Y78         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.244 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[15]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.244    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[15]_i_4_n_0
    SLICE_X61Y79         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.358 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[19]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.358    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[19]_i_4_n_0
    SLICE_X61Y80         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.472 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[23]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.472    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[23]_i_4_n_0
    SLICE_X61Y81         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.586 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[27]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.586    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[27]_i_4_n_0
    SLICE_X61Y82         CARRY4 (Prop_carry4_CI_O[3])
                                                      0.313    16.899 f  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[31]_i_5/O[3]
                         net (fo=2, routed)           0.763    17.662    VexRiscv/IBusCachedPlugin_cache/_zz_execute_SrcPlugin_addSub[19]
    SLICE_X62Y77         LUT5 (Prop_lut5_I1_O)        0.306    17.968 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[0]_i_7/O
                         net (fo=2, routed)           0.464    18.432    VexRiscv/IBusCachedPlugin_cache/decode_to_execute_SRC2_FORCE_ZERO_reg
    SLICE_X62Y77         LUT6 (Prop_lut6_I1_O)        0.124    18.556 r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_58/O
                         net (fo=1, routed)           0.707    19.263    VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_58_n_0
    SLICE_X67Y71         LUT5 (Prop_lut5_I1_O)        0.124    19.387 f  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_35/O
                         net (fo=6, routed)           1.050    20.438    VexRiscv/IBusCachedPlugin_cache_n_229
    SLICE_X78Y69         LUT2 (Prop_lut2_I1_O)        0.124    20.562 r  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[1]_i_3/O
                         net (fo=35, routed)          0.900    21.462    VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[1]_i_3_n_0
    SLICE_X84Y69         LUT2 (Prop_lut2_I1_O)        0.124    21.586 f  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[31]_i_5/O
                         net (fo=43, routed)          0.556    22.142    VexRiscv/IBusCachedPlugin_cache/CsrPlugin_exceptionPortCtrl_exceptionContext_code_reg[0]_0
    SLICE_X85Y69         LUT3 (Prop_lut3_I2_O)        0.124    22.266 r  VexRiscv/IBusCachedPlugin_cache/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[31]_i_1/O
                         net (fo=36, routed)          1.546    23.812    VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr
    SLICE_X68Y76         FDRE                                         r  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[28]/CE
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                     13.333    13.333 r  
    E3                                                0.000    13.333 r  clk100 (IN)
                         net (fo=0)                   0.000    13.333    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411    14.745 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920    16.665    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091    16.756 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    18.969    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    19.069 r  clk100_inst/O
                         net (fo=9, routed)           1.645    20.714    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.083    20.797 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           1.923    22.721    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.091    22.812 r  BUFG/O
                         net (fo=4933, routed)        1.494    24.306    VexRiscv/stageB_flusher_counter_reg[0]
    SLICE_X68Y76         FDRE                                         r  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[28]/C
                         clock pessimism              0.850    25.156    
                         clock uncertainty           -0.070    25.086    
    SLICE_X68Y76         FDRE (Setup_fdre_C_CE)      -0.205    24.881    VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[28]
  -------------------------------------------------------------------
                         required time                         24.881    
                         arrival time                         -23.812    
  -------------------------------------------------------------------
                         slack                                  1.069    

Slack (MET) :             1.071ns  (required time - arrival time)
  Source:                 VexRiscv/decode_to_execute_RS2_reg[0]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[21]/CE
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            13.333ns  (soc_crg_clkout0 rise@13.333ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        11.877ns  (logic 3.283ns (27.641%)  route 8.594ns (72.359%))
  Logic Levels:           16  (CARRY4=8 LUT2=2 LUT3=1 LUT5=3 LUT6=2)
  Clock Path Skew:        -0.110ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    10.974ns = ( 24.307 - 13.333 ) 
    Source Clock Delay      (SCD):    11.933ns
    Clock Pessimism Removal (CPR):    0.850ns
  Clock Uncertainty:      0.070ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.121ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG/O
                         net (fo=4933, routed)        1.613    11.933    VexRiscv/stageB_flusher_counter_reg[0]
    SLICE_X51Y72         FDRE                                         r  VexRiscv/decode_to_execute_RS2_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X51Y72         FDRE (Prop_fdre_C_Q)         0.456    12.389 f  VexRiscv/decode_to_execute_RS2_reg[0]/Q
                         net (fo=10, routed)          1.185    13.574    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[31]_i_3[0]
    SLICE_X63Y72         LUT5 (Prop_lut5_I1_O)        0.124    13.698 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_SHIFT_RIGHT[31]_i_5/O
                         net (fo=35, routed)          0.802    14.500    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19_0
    SLICE_X60Y75         LUT6 (Prop_lut6_I4_O)        0.124    14.624 r  VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_26/O
                         net (fo=1, routed)           0.622    15.246    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_26_n_0
    SLICE_X61Y75         CARRY4 (Prop_carry4_S[0]_CO[3])
                                                      0.656    15.902 r  VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19/CO[3]
                         net (fo=1, routed)           0.000    15.902    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19_n_0
    SLICE_X61Y76         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.016 r  VexRiscv/dataCache_1/ways_0_tags_reg_i_21/CO[3]
                         net (fo=1, routed)           0.000    16.016    VexRiscv/dataCache_1/ways_0_tags_reg_i_21_n_0
    SLICE_X61Y77         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.130 r  VexRiscv/dataCache_1/ways_0_tags_reg_i_20/CO[3]
                         net (fo=1, routed)           0.000    16.130    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[12]_i_2[0]
    SLICE_X61Y78         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.244 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[15]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.244    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[15]_i_4_n_0
    SLICE_X61Y79         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.358 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[19]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.358    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[19]_i_4_n_0
    SLICE_X61Y80         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.472 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[23]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.472    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[23]_i_4_n_0
    SLICE_X61Y81         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.586 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[27]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.586    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[27]_i_4_n_0
    SLICE_X61Y82         CARRY4 (Prop_carry4_CI_O[3])
                                                      0.313    16.899 f  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[31]_i_5/O[3]
                         net (fo=2, routed)           0.763    17.662    VexRiscv/IBusCachedPlugin_cache/_zz_execute_SrcPlugin_addSub[19]
    SLICE_X62Y77         LUT5 (Prop_lut5_I1_O)        0.306    17.968 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[0]_i_7/O
                         net (fo=2, routed)           0.464    18.432    VexRiscv/IBusCachedPlugin_cache/decode_to_execute_SRC2_FORCE_ZERO_reg
    SLICE_X62Y77         LUT6 (Prop_lut6_I1_O)        0.124    18.556 r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_58/O
                         net (fo=1, routed)           0.707    19.263    VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_58_n_0
    SLICE_X67Y71         LUT5 (Prop_lut5_I1_O)        0.124    19.387 f  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_35/O
                         net (fo=6, routed)           1.050    20.438    VexRiscv/IBusCachedPlugin_cache_n_229
    SLICE_X78Y69         LUT2 (Prop_lut2_I1_O)        0.124    20.562 r  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[1]_i_3/O
                         net (fo=35, routed)          0.900    21.462    VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[1]_i_3_n_0
    SLICE_X84Y69         LUT2 (Prop_lut2_I1_O)        0.124    21.586 f  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[31]_i_5/O
                         net (fo=43, routed)          0.556    22.142    VexRiscv/IBusCachedPlugin_cache/CsrPlugin_exceptionPortCtrl_exceptionContext_code_reg[0]_0
    SLICE_X85Y69         LUT3 (Prop_lut3_I2_O)        0.124    22.266 r  VexRiscv/IBusCachedPlugin_cache/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[31]_i_1/O
                         net (fo=36, routed)          1.545    23.811    VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr
    SLICE_X64Y77         FDRE                                         r  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[21]/CE
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                     13.333    13.333 r  
    E3                                                0.000    13.333 r  clk100 (IN)
                         net (fo=0)                   0.000    13.333    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411    14.745 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920    16.665    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091    16.756 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    18.969    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    19.069 r  clk100_inst/O
                         net (fo=9, routed)           1.645    20.714    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.083    20.797 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           1.923    22.721    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.091    22.812 r  BUFG/O
                         net (fo=4933, routed)        1.495    24.307    VexRiscv/stageB_flusher_counter_reg[0]
    SLICE_X64Y77         FDRE                                         r  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[21]/C
                         clock pessimism              0.850    25.157    
                         clock uncertainty           -0.070    25.087    
    SLICE_X64Y77         FDRE (Setup_fdre_C_CE)      -0.205    24.882    VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[21]
  -------------------------------------------------------------------
                         required time                         24.882    
                         arrival time                         -23.811    
  -------------------------------------------------------------------
                         slack                                  1.071    

Slack (MET) :             1.071ns  (required time - arrival time)
  Source:                 VexRiscv/decode_to_execute_RS2_reg[0]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[23]/CE
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            13.333ns  (soc_crg_clkout0 rise@13.333ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        11.877ns  (logic 3.283ns (27.641%)  route 8.594ns (72.359%))
  Logic Levels:           16  (CARRY4=8 LUT2=2 LUT3=1 LUT5=3 LUT6=2)
  Clock Path Skew:        -0.110ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    10.974ns = ( 24.307 - 13.333 ) 
    Source Clock Delay      (SCD):    11.933ns
    Clock Pessimism Removal (CPR):    0.850ns
  Clock Uncertainty:      0.070ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.121ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG/O
                         net (fo=4933, routed)        1.613    11.933    VexRiscv/stageB_flusher_counter_reg[0]
    SLICE_X51Y72         FDRE                                         r  VexRiscv/decode_to_execute_RS2_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X51Y72         FDRE (Prop_fdre_C_Q)         0.456    12.389 f  VexRiscv/decode_to_execute_RS2_reg[0]/Q
                         net (fo=10, routed)          1.185    13.574    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[31]_i_3[0]
    SLICE_X63Y72         LUT5 (Prop_lut5_I1_O)        0.124    13.698 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_SHIFT_RIGHT[31]_i_5/O
                         net (fo=35, routed)          0.802    14.500    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19_0
    SLICE_X60Y75         LUT6 (Prop_lut6_I4_O)        0.124    14.624 r  VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_26/O
                         net (fo=1, routed)           0.622    15.246    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_26_n_0
    SLICE_X61Y75         CARRY4 (Prop_carry4_S[0]_CO[3])
                                                      0.656    15.902 r  VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19/CO[3]
                         net (fo=1, routed)           0.000    15.902    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19_n_0
    SLICE_X61Y76         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.016 r  VexRiscv/dataCache_1/ways_0_tags_reg_i_21/CO[3]
                         net (fo=1, routed)           0.000    16.016    VexRiscv/dataCache_1/ways_0_tags_reg_i_21_n_0
    SLICE_X61Y77         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.130 r  VexRiscv/dataCache_1/ways_0_tags_reg_i_20/CO[3]
                         net (fo=1, routed)           0.000    16.130    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[12]_i_2[0]
    SLICE_X61Y78         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.244 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[15]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.244    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[15]_i_4_n_0
    SLICE_X61Y79         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.358 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[19]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.358    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[19]_i_4_n_0
    SLICE_X61Y80         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.472 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[23]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.472    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[23]_i_4_n_0
    SLICE_X61Y81         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.586 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[27]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.586    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[27]_i_4_n_0
    SLICE_X61Y82         CARRY4 (Prop_carry4_CI_O[3])
                                                      0.313    16.899 f  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[31]_i_5/O[3]
                         net (fo=2, routed)           0.763    17.662    VexRiscv/IBusCachedPlugin_cache/_zz_execute_SrcPlugin_addSub[19]
    SLICE_X62Y77         LUT5 (Prop_lut5_I1_O)        0.306    17.968 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[0]_i_7/O
                         net (fo=2, routed)           0.464    18.432    VexRiscv/IBusCachedPlugin_cache/decode_to_execute_SRC2_FORCE_ZERO_reg
    SLICE_X62Y77         LUT6 (Prop_lut6_I1_O)        0.124    18.556 r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_58/O
                         net (fo=1, routed)           0.707    19.263    VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_58_n_0
    SLICE_X67Y71         LUT5 (Prop_lut5_I1_O)        0.124    19.387 f  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_35/O
                         net (fo=6, routed)           1.050    20.438    VexRiscv/IBusCachedPlugin_cache_n_229
    SLICE_X78Y69         LUT2 (Prop_lut2_I1_O)        0.124    20.562 r  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[1]_i_3/O
                         net (fo=35, routed)          0.900    21.462    VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[1]_i_3_n_0
    SLICE_X84Y69         LUT2 (Prop_lut2_I1_O)        0.124    21.586 f  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[31]_i_5/O
                         net (fo=43, routed)          0.556    22.142    VexRiscv/IBusCachedPlugin_cache/CsrPlugin_exceptionPortCtrl_exceptionContext_code_reg[0]_0
    SLICE_X85Y69         LUT3 (Prop_lut3_I2_O)        0.124    22.266 r  VexRiscv/IBusCachedPlugin_cache/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[31]_i_1/O
                         net (fo=36, routed)          1.545    23.811    VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr
    SLICE_X64Y77         FDRE                                         r  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[23]/CE
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                     13.333    13.333 r  
    E3                                                0.000    13.333 r  clk100 (IN)
                         net (fo=0)                   0.000    13.333    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411    14.745 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920    16.665    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091    16.756 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    18.969    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    19.069 r  clk100_inst/O
                         net (fo=9, routed)           1.645    20.714    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.083    20.797 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           1.923    22.721    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.091    22.812 r  BUFG/O
                         net (fo=4933, routed)        1.495    24.307    VexRiscv/stageB_flusher_counter_reg[0]
    SLICE_X64Y77         FDRE                                         r  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[23]/C
                         clock pessimism              0.850    25.157    
                         clock uncertainty           -0.070    25.087    
    SLICE_X64Y77         FDRE (Setup_fdre_C_CE)      -0.205    24.882    VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[23]
  -------------------------------------------------------------------
                         required time                         24.882    
                         arrival time                         -23.811    
  -------------------------------------------------------------------
                         slack                                  1.071    

Slack (MET) :             1.071ns  (required time - arrival time)
  Source:                 VexRiscv/decode_to_execute_RS2_reg[0]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[30]/CE
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            13.333ns  (soc_crg_clkout0 rise@13.333ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        11.877ns  (logic 3.283ns (27.641%)  route 8.594ns (72.359%))
  Logic Levels:           16  (CARRY4=8 LUT2=2 LUT3=1 LUT5=3 LUT6=2)
  Clock Path Skew:        -0.110ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    10.974ns = ( 24.307 - 13.333 ) 
    Source Clock Delay      (SCD):    11.933ns
    Clock Pessimism Removal (CPR):    0.850ns
  Clock Uncertainty:      0.070ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.121ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG/O
                         net (fo=4933, routed)        1.613    11.933    VexRiscv/stageB_flusher_counter_reg[0]
    SLICE_X51Y72         FDRE                                         r  VexRiscv/decode_to_execute_RS2_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X51Y72         FDRE (Prop_fdre_C_Q)         0.456    12.389 f  VexRiscv/decode_to_execute_RS2_reg[0]/Q
                         net (fo=10, routed)          1.185    13.574    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[31]_i_3[0]
    SLICE_X63Y72         LUT5 (Prop_lut5_I1_O)        0.124    13.698 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_SHIFT_RIGHT[31]_i_5/O
                         net (fo=35, routed)          0.802    14.500    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19_0
    SLICE_X60Y75         LUT6 (Prop_lut6_I4_O)        0.124    14.624 r  VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_26/O
                         net (fo=1, routed)           0.622    15.246    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_26_n_0
    SLICE_X61Y75         CARRY4 (Prop_carry4_S[0]_CO[3])
                                                      0.656    15.902 r  VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19/CO[3]
                         net (fo=1, routed)           0.000    15.902    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19_n_0
    SLICE_X61Y76         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.016 r  VexRiscv/dataCache_1/ways_0_tags_reg_i_21/CO[3]
                         net (fo=1, routed)           0.000    16.016    VexRiscv/dataCache_1/ways_0_tags_reg_i_21_n_0
    SLICE_X61Y77         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.130 r  VexRiscv/dataCache_1/ways_0_tags_reg_i_20/CO[3]
                         net (fo=1, routed)           0.000    16.130    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[12]_i_2[0]
    SLICE_X61Y78         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.244 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[15]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.244    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[15]_i_4_n_0
    SLICE_X61Y79         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.358 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[19]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.358    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[19]_i_4_n_0
    SLICE_X61Y80         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.472 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[23]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.472    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[23]_i_4_n_0
    SLICE_X61Y81         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.586 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[27]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.586    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[27]_i_4_n_0
    SLICE_X61Y82         CARRY4 (Prop_carry4_CI_O[3])
                                                      0.313    16.899 f  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[31]_i_5/O[3]
                         net (fo=2, routed)           0.763    17.662    VexRiscv/IBusCachedPlugin_cache/_zz_execute_SrcPlugin_addSub[19]
    SLICE_X62Y77         LUT5 (Prop_lut5_I1_O)        0.306    17.968 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[0]_i_7/O
                         net (fo=2, routed)           0.464    18.432    VexRiscv/IBusCachedPlugin_cache/decode_to_execute_SRC2_FORCE_ZERO_reg
    SLICE_X62Y77         LUT6 (Prop_lut6_I1_O)        0.124    18.556 r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_58/O
                         net (fo=1, routed)           0.707    19.263    VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_58_n_0
    SLICE_X67Y71         LUT5 (Prop_lut5_I1_O)        0.124    19.387 f  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_35/O
                         net (fo=6, routed)           1.050    20.438    VexRiscv/IBusCachedPlugin_cache_n_229
    SLICE_X78Y69         LUT2 (Prop_lut2_I1_O)        0.124    20.562 r  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[1]_i_3/O
                         net (fo=35, routed)          0.900    21.462    VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[1]_i_3_n_0
    SLICE_X84Y69         LUT2 (Prop_lut2_I1_O)        0.124    21.586 f  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[31]_i_5/O
                         net (fo=43, routed)          0.556    22.142    VexRiscv/IBusCachedPlugin_cache/CsrPlugin_exceptionPortCtrl_exceptionContext_code_reg[0]_0
    SLICE_X85Y69         LUT3 (Prop_lut3_I2_O)        0.124    22.266 r  VexRiscv/IBusCachedPlugin_cache/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr[31]_i_1/O
                         net (fo=36, routed)          1.545    23.811    VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr
    SLICE_X64Y77         FDRE                                         r  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[30]/CE
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                     13.333    13.333 r  
    E3                                                0.000    13.333 r  clk100 (IN)
                         net (fo=0)                   0.000    13.333    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411    14.745 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920    16.665    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091    16.756 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    18.969    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    19.069 r  clk100_inst/O
                         net (fo=9, routed)           1.645    20.714    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.083    20.797 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           1.923    22.721    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.091    22.812 r  BUFG/O
                         net (fo=4933, routed)        1.495    24.307    VexRiscv/stageB_flusher_counter_reg[0]
    SLICE_X64Y77         FDRE                                         r  VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[30]/C
                         clock pessimism              0.850    25.157    
                         clock uncertainty           -0.070    25.087    
    SLICE_X64Y77         FDRE (Setup_fdre_C_CE)      -0.205    24.882    VexRiscv/CsrPlugin_exceptionPortCtrl_exceptionContext_badAddr_reg[30]
  -------------------------------------------------------------------
                         required time                         24.882    
                         arrival time                         -23.811    
  -------------------------------------------------------------------
                         slack                                  1.071    

Slack (MET) :             1.073ns  (required time - arrival time)
  Source:                 VexRiscv/decode_to_execute_INSTRUCTION_reg[13]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            VexRiscv/RegFilePlugin_regFile_reg_2/ADDRARDADDR[7]
                            (rising edge-triggered cell RAMB18E1 clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            13.333ns  (soc_crg_clkout0 rise@13.333ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        11.415ns  (logic 2.891ns (25.326%)  route 8.524ns (74.674%))
  Logic Levels:           12  (LUT3=3 LUT5=1 LUT6=7 MUXF7=1)
  Clock Path Skew:        0.014ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    11.014ns = ( 24.347 - 13.333 ) 
    Source Clock Delay      (SCD):    11.938ns
    Clock Pessimism Removal (CPR):    0.939ns
  Clock Uncertainty:      0.070ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.121ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG/O
                         net (fo=4933, routed)        1.618    11.938    VexRiscv/stageB_flusher_counter_reg[0]
    SLICE_X63Y69         FDRE                                         r  VexRiscv/decode_to_execute_INSTRUCTION_reg[13]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X63Y69         FDRE (Prop_fdre_C_Q)         0.456    12.394 f  VexRiscv/decode_to_execute_INSTRUCTION_reg[13]/Q
                         net (fo=182, routed)         0.981    13.375    VexRiscv/CfuPlugin_bus_cmd_payload_function_id[1]
    SLICE_X61Y69         LUT3 (Prop_lut3_I1_O)        0.152    13.527 f  VexRiscv/captured[6]_i_3/O
                         net (fo=4, routed)           0.631    14.159    VexRiscv/decode_to_execute_INSTRUCTION_reg[14]_0
    SLICE_X61Y68         LUT6 (Prop_lut6_I5_O)        0.326    14.485 r  VexRiscv/captured[6]_i_1/O
                         net (fo=220, routed)         0.916    15.400    VexRiscv/$signal$2
    SLICE_X64Y67         LUT3 (Prop_lut3_I1_O)        0.150    15.550 f  VexRiscv/was_updated_i_3/O
                         net (fo=10, routed)          1.035    16.585    VexRiscv/Cfu/fn0/f7buf/$1[2]
    SLICE_X63Y65         LUT5 (Prop_lut5_I4_O)        0.352    16.937 r  VexRiscv/waiting_i_3/O
                         net (fo=4, routed)           0.454    17.391    VexRiscv/dataCache_1/stageA_mask[3]_i_12_0
    SLICE_X62Y65         LUT6 (Prop_lut6_I3_O)        0.326    17.717 r  VexRiscv/dataCache_1/stageA_mask[3]_i_19/O
                         net (fo=1, routed)           0.635    18.352    VexRiscv/dataCache_1/stageA_mask[3]_i_19_n_0
    SLICE_X61Y66         LUT6 (Prop_lut6_I5_O)        0.124    18.476 r  VexRiscv/dataCache_1/stageA_mask[3]_i_12/O
                         net (fo=1, routed)           0.000    18.476    VexRiscv/dataCache_1/stageA_mask[3]_i_12_n_0
    SLICE_X61Y66         MUXF7 (Prop_muxf7_I1_O)      0.217    18.693 r  VexRiscv/dataCache_1/stageA_mask_reg[3]_i_7/O
                         net (fo=3, routed)           0.610    19.302    VexRiscv/dataCache_1/decode_to_execute_INSTRUCTION_reg[30]
    SLICE_X60Y67         LUT6 (Prop_lut6_I0_O)        0.299    19.601 r  VexRiscv/dataCache_1/stageA_mask[3]_i_3/O
                         net (fo=1, routed)           0.282    19.883    VexRiscv/dataCache_1/soc_basesoc_vexriscv_cfu_bus_rsp_valid
    SLICE_X59Y67         LUT6 (Prop_lut6_I2_O)        0.124    20.007 r  VexRiscv/dataCache_1/stageA_mask[3]_i_1/O
                         net (fo=264, routed)         0.563    20.570    VexRiscv/dataCache_1/memory_DivPlugin_div_counter_willClear
    SLICE_X61Y68         LUT6 (Prop_lut6_I3_O)        0.124    20.694 r  VexRiscv/dataCache_1/decode_to_execute_ENV_CTRL[1]_i_1/O
                         net (fo=216, routed)         0.858    21.552    VexRiscv/IBusCachedPlugin_cache/when_CsrPlugin_l922_1
    SLICE_X68Y67         LUT6 (Prop_lut6_I4_O)        0.124    21.676 r  VexRiscv/IBusCachedPlugin_cache/RegFilePlugin_regFile_reg_1_i_44/O
                         net (fo=13, routed)          0.770    22.446    VexRiscv/IBusCachedPlugin_cache/io_cpu_fetch_data_regNextWhen_reg[4]_0
    SLICE_X66Y69         LUT3 (Prop_lut3_I1_O)        0.117    22.563 r  VexRiscv/IBusCachedPlugin_cache/RegFilePlugin_regFile_reg_2_i_3/O
                         net (fo=1, routed)           0.790    23.353    VexRiscv/decode_RegFilePlugin_regFileReadAddress2[2]
    RAMB18_X1Y29         RAMB18E1                                     r  VexRiscv/RegFilePlugin_regFile_reg_2/ADDRARDADDR[7]
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                     13.333    13.333 r  
    E3                                                0.000    13.333 r  clk100 (IN)
                         net (fo=0)                   0.000    13.333    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411    14.745 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920    16.665    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091    16.756 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    18.969    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    19.069 r  clk100_inst/O
                         net (fo=9, routed)           1.645    20.714    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.083    20.797 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           1.923    22.721    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.091    22.812 r  BUFG/O
                         net (fo=4933, routed)        1.536    24.347    VexRiscv/stageB_flusher_counter_reg[0]
    RAMB18_X1Y29         RAMB18E1                                     r  VexRiscv/RegFilePlugin_regFile_reg_2/CLKARDCLK
                         clock pessimism              0.939    25.286    
                         clock uncertainty           -0.070    25.216    
    RAMB18_X1Y29         RAMB18E1 (Setup_ramb18e1_CLKARDCLK_ADDRARDADDR[7])
                                                     -0.790    24.426    VexRiscv/RegFilePlugin_regFile_reg_2
  -------------------------------------------------------------------
                         required time                         24.426    
                         arrival time                         -23.353    
  -------------------------------------------------------------------
                         slack                                  1.073    

Slack (MET) :             1.078ns  (required time - arrival time)
  Source:                 VexRiscv/decode_to_execute_RS2_reg[0]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            VexRiscv/IBusCachedPlugin_cache/banks_0_reg/ADDRBWRADDR[14]
                            (rising edge-triggered cell RAMB36E1 clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            13.333ns  (soc_crg_clkout0 rise@13.333ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        11.650ns  (logic 3.483ns (29.897%)  route 8.167ns (70.104%))
  Logic Levels:           16  (CARRY4=8 LUT4=1 LUT5=3 LUT6=4)
  Clock Path Skew:        0.030ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    11.114ns = ( 24.447 - 13.333 ) 
    Source Clock Delay      (SCD):    11.933ns
    Clock Pessimism Removal (CPR):    0.850ns
  Clock Uncertainty:      0.070ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.121ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG/O
                         net (fo=4933, routed)        1.613    11.933    VexRiscv/stageB_flusher_counter_reg[0]
    SLICE_X51Y72         FDRE                                         r  VexRiscv/decode_to_execute_RS2_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X51Y72         FDRE (Prop_fdre_C_Q)         0.456    12.389 f  VexRiscv/decode_to_execute_RS2_reg[0]/Q
                         net (fo=10, routed)          1.185    13.574    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[31]_i_3[0]
    SLICE_X63Y72         LUT5 (Prop_lut5_I1_O)        0.124    13.698 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_SHIFT_RIGHT[31]_i_5/O
                         net (fo=35, routed)          0.802    14.500    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19_0
    SLICE_X60Y75         LUT6 (Prop_lut6_I4_O)        0.124    14.624 r  VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_26/O
                         net (fo=1, routed)           0.622    15.246    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_26_n_0
    SLICE_X61Y75         CARRY4 (Prop_carry4_S[0]_CO[3])
                                                      0.656    15.902 r  VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19/CO[3]
                         net (fo=1, routed)           0.000    15.902    VexRiscv/dataCache_1/ways_0_data_symbol0_reg_i_19_n_0
    SLICE_X61Y76         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.016 r  VexRiscv/dataCache_1/ways_0_tags_reg_i_21/CO[3]
                         net (fo=1, routed)           0.000    16.016    VexRiscv/dataCache_1/ways_0_tags_reg_i_21_n_0
    SLICE_X61Y77         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.130 r  VexRiscv/dataCache_1/ways_0_tags_reg_i_20/CO[3]
                         net (fo=1, routed)           0.000    16.130    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[12]_i_2[0]
    SLICE_X61Y78         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.244 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[15]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.244    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[15]_i_4_n_0
    SLICE_X61Y79         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.358 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[19]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.358    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[19]_i_4_n_0
    SLICE_X61Y80         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.472 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[23]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.472    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[23]_i_4_n_0
    SLICE_X61Y81         CARRY4 (Prop_carry4_CI_CO[3])
                                                      0.114    16.586 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[27]_i_4/CO[3]
                         net (fo=1, routed)           0.000    16.586    VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[27]_i_4_n_0
    SLICE_X61Y82         CARRY4 (Prop_carry4_CI_O[3])
                                                      0.313    16.899 f  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA_reg[31]_i_5/O[3]
                         net (fo=2, routed)           0.763    17.662    VexRiscv/IBusCachedPlugin_cache/_zz_execute_SrcPlugin_addSub[19]
    SLICE_X62Y77         LUT5 (Prop_lut5_I1_O)        0.306    17.968 r  VexRiscv/IBusCachedPlugin_cache/execute_to_memory_REGFILE_WRITE_DATA[0]_i_7/O
                         net (fo=2, routed)           0.464    18.432    VexRiscv/IBusCachedPlugin_cache/decode_to_execute_SRC2_FORCE_ZERO_reg
    SLICE_X62Y77         LUT6 (Prop_lut6_I1_O)        0.124    18.556 r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_58/O
                         net (fo=1, routed)           0.707    19.263    VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_58_n_0
    SLICE_X67Y71         LUT5 (Prop_lut5_I1_O)        0.124    19.387 f  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_35/O
                         net (fo=6, routed)           1.046    20.434    VexRiscv/IBusCachedPlugin_cache/decode_to_execute_BRANCH_CTRL_reg[1]
    SLICE_X78Y68         LUT4 (Prop_lut4_I1_O)        0.117    20.551 r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_39/O
                         net (fo=30, routed)          1.076    21.627    VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_39_n_0
    SLICE_X69Y71         LUT6 (Prop_lut6_I2_O)        0.331    21.958 f  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_16/O
                         net (fo=2, routed)           0.438    22.396    VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_16_n_0
    SLICE_X68Y70         LUT6 (Prop_lut6_I5_O)        0.124    22.520 r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg_i_2/O
                         net (fo=2, routed)           1.064    23.584    VexRiscv/IBusCachedPlugin_cache/IBusCachedPlugin_iBusRsp_stages_0_input_payload[11]
    RAMB36_X3Y13         RAMB36E1                                     r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg/ADDRBWRADDR[14]
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                     13.333    13.333 r  
    E3                                                0.000    13.333 r  clk100 (IN)
                         net (fo=0)                   0.000    13.333    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411    14.745 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920    16.665    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091    16.756 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    18.969    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    19.069 r  clk100_inst/O
                         net (fo=9, routed)           1.645    20.714    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.083    20.797 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           1.923    22.721    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.091    22.812 r  BUFG/O
                         net (fo=4933, routed)        1.636    24.447    VexRiscv/IBusCachedPlugin_cache/ways_0_tags_reg_0
    RAMB36_X3Y13         RAMB36E1                                     r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg/CLKBWRCLK
                         clock pessimism              0.850    25.297    
                         clock uncertainty           -0.070    25.227    
    RAMB36_X3Y13         RAMB36E1 (Setup_ramb36e1_CLKBWRCLK_ADDRBWRADDR[14])
                                                     -0.566    24.661    VexRiscv/IBusCachedPlugin_cache/banks_0_reg
  -------------------------------------------------------------------
                         required time                         24.661    
                         arrival time                         -23.584    
  -------------------------------------------------------------------
                         slack                                  1.078    





Min Delay Paths
--------------------------------------------------------------------------------------
Slack (MET) :             0.032ns  (arrival time - required time)
  Source:                 soc_basesoc_timer_value_reg[27]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            soc_basesoc_timer_value_status_reg[27]/D
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout0 rise@0.000ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        0.365ns  (logic 0.141ns (38.608%)  route 0.224ns (61.392%))
  Logic Levels:           0  
  Clock Path Skew:        0.270ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.065ns
    Source Clock Delay      (SCD):    4.030ns
    Clock Pessimism Removal (CPR):    0.764ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG/O
                         net (fo=4933, routed)        0.601     4.030    sys_clk
    SLICE_X81Y99         FDRE                                         r  soc_basesoc_timer_value_reg[27]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X81Y99         FDRE (Prop_fdre_C_Q)         0.141     4.171 r  soc_basesoc_timer_value_reg[27]/Q
                         net (fo=4, routed)           0.224     4.395    soc_basesoc_timer_value_reg_n_0_[27]
    SLICE_X80Y100        FDRE                                         r  soc_basesoc_timer_value_status_reg[27]/D
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG/O
                         net (fo=4933, routed)        0.870     5.065    sys_clk
    SLICE_X80Y100        FDRE                                         r  soc_basesoc_timer_value_status_reg[27]/C
                         clock pessimism             -0.764     4.300    
    SLICE_X80Y100        FDRE (Hold_fdre_C_D)         0.063     4.363    soc_basesoc_timer_value_status_reg[27]
  -------------------------------------------------------------------
                         required time                         -4.363    
                         arrival time                           4.395    
  -------------------------------------------------------------------
                         slack                                  0.032    

Slack (MET) :             0.051ns  (arrival time - required time)
  Source:                 VexRiscv/iBusWishbone_DAT_MISO_regNext_reg[2]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            VexRiscv/IBusCachedPlugin_cache/banks_0_reg/DIADI[2]
                            (rising edge-triggered cell RAMB36E1 clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout0 rise@0.000ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        0.259ns  (logic 0.141ns (54.387%)  route 0.118ns (45.613%))
  Logic Levels:           0  
  Clock Path Skew:        0.053ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.099ns
    Source Clock Delay      (SCD):    4.025ns
    Clock Pessimism Removal (CPR):    1.020ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG/O
                         net (fo=4933, routed)        0.596     4.025    VexRiscv/stageB_flusher_counter_reg[0]
    SLICE_X81Y64         FDRE                                         r  VexRiscv/iBusWishbone_DAT_MISO_regNext_reg[2]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X81Y64         FDRE (Prop_fdre_C_Q)         0.141     4.166 r  VexRiscv/iBusWishbone_DAT_MISO_regNext_reg[2]/Q
                         net (fo=3, routed)           0.118     4.284    VexRiscv/IBusCachedPlugin_cache/iBusWishbone_DAT_MISO_regNext[2]
    RAMB36_X3Y13         RAMB36E1                                     r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg/DIADI[2]
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG/O
                         net (fo=4933, routed)        0.905     5.099    VexRiscv/IBusCachedPlugin_cache/ways_0_tags_reg_0
    RAMB36_X3Y13         RAMB36E1                                     r  VexRiscv/IBusCachedPlugin_cache/banks_0_reg/CLKARDCLK
                         clock pessimism             -1.020     4.079    
    RAMB36_X3Y13         RAMB36E1 (Hold_ramb36e1_CLKARDCLK_DIADI[2])
                                                      0.155     4.234    VexRiscv/IBusCachedPlugin_cache/banks_0_reg
  -------------------------------------------------------------------
                         required time                         -4.234    
                         arrival time                           4.284    
  -------------------------------------------------------------------
                         slack                                  0.051    

Slack (MET) :             0.059ns  (arrival time - required time)
  Source:                 soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            storage_3_reg_0_7_12_17/RAMA/WADR0
                            (rising edge-triggered cell RAMD32 clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout0 rise@0.000ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        0.382ns  (logic 0.141ns (36.945%)  route 0.241ns (63.055%))
  Logic Levels:           0  
  Clock Path Skew:        0.013ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.030ns
    Source Clock Delay      (SCD):    3.994ns
    Clock Pessimism Removal (CPR):    1.022ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG/O
                         net (fo=4933, routed)        0.565     3.994    sys_clk
    SLICE_X61Y97         FDRE                                         r  soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X61Y97         FDRE (Prop_fdre_C_Q)         0.141     4.135 r  soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/Q
                         net (fo=35, routed)          0.241     4.376    storage_3_reg_0_7_12_17/ADDRD0
    SLICE_X60Y97         RAMD32                                       r  storage_3_reg_0_7_12_17/RAMA/WADR0
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG/O
                         net (fo=4933, routed)        0.836     5.030    storage_3_reg_0_7_12_17/WCLK
    SLICE_X60Y97         RAMD32                                       r  storage_3_reg_0_7_12_17/RAMA/CLK
                         clock pessimism             -1.022     4.007    
    SLICE_X60Y97         RAMD32 (Hold_ramd32_CLK_WADR0)
                                                      0.310     4.317    storage_3_reg_0_7_12_17/RAMA
  -------------------------------------------------------------------
                         required time                         -4.317    
                         arrival time                           4.376    
  -------------------------------------------------------------------
                         slack                                  0.059    

Slack (MET) :             0.059ns  (arrival time - required time)
  Source:                 soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            storage_3_reg_0_7_12_17/RAMA_D1/WADR0
                            (rising edge-triggered cell RAMD32 clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout0 rise@0.000ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        0.382ns  (logic 0.141ns (36.945%)  route 0.241ns (63.055%))
  Logic Levels:           0  
  Clock Path Skew:        0.013ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.030ns
    Source Clock Delay      (SCD):    3.994ns
    Clock Pessimism Removal (CPR):    1.022ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG/O
                         net (fo=4933, routed)        0.565     3.994    sys_clk
    SLICE_X61Y97         FDRE                                         r  soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X61Y97         FDRE (Prop_fdre_C_Q)         0.141     4.135 r  soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/Q
                         net (fo=35, routed)          0.241     4.376    storage_3_reg_0_7_12_17/ADDRD0
    SLICE_X60Y97         RAMD32                                       r  storage_3_reg_0_7_12_17/RAMA_D1/WADR0
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG/O
                         net (fo=4933, routed)        0.836     5.030    storage_3_reg_0_7_12_17/WCLK
    SLICE_X60Y97         RAMD32                                       r  storage_3_reg_0_7_12_17/RAMA_D1/CLK
                         clock pessimism             -1.022     4.007    
    SLICE_X60Y97         RAMD32 (Hold_ramd32_CLK_WADR0)
                                                      0.310     4.317    storage_3_reg_0_7_12_17/RAMA_D1
  -------------------------------------------------------------------
                         required time                         -4.317    
                         arrival time                           4.376    
  -------------------------------------------------------------------
                         slack                                  0.059    

Slack (MET) :             0.059ns  (arrival time - required time)
  Source:                 soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            storage_3_reg_0_7_12_17/RAMB/WADR0
                            (rising edge-triggered cell RAMD32 clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout0 rise@0.000ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        0.382ns  (logic 0.141ns (36.945%)  route 0.241ns (63.055%))
  Logic Levels:           0  
  Clock Path Skew:        0.013ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.030ns
    Source Clock Delay      (SCD):    3.994ns
    Clock Pessimism Removal (CPR):    1.022ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG/O
                         net (fo=4933, routed)        0.565     3.994    sys_clk
    SLICE_X61Y97         FDRE                                         r  soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X61Y97         FDRE (Prop_fdre_C_Q)         0.141     4.135 r  soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/Q
                         net (fo=35, routed)          0.241     4.376    storage_3_reg_0_7_12_17/ADDRD0
    SLICE_X60Y97         RAMD32                                       r  storage_3_reg_0_7_12_17/RAMB/WADR0
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG/O
                         net (fo=4933, routed)        0.836     5.030    storage_3_reg_0_7_12_17/WCLK
    SLICE_X60Y97         RAMD32                                       r  storage_3_reg_0_7_12_17/RAMB/CLK
                         clock pessimism             -1.022     4.007    
    SLICE_X60Y97         RAMD32 (Hold_ramd32_CLK_WADR0)
                                                      0.310     4.317    storage_3_reg_0_7_12_17/RAMB
  -------------------------------------------------------------------
                         required time                         -4.317    
                         arrival time                           4.376    
  -------------------------------------------------------------------
                         slack                                  0.059    

Slack (MET) :             0.059ns  (arrival time - required time)
  Source:                 soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            storage_3_reg_0_7_12_17/RAMB_D1/WADR0
                            (rising edge-triggered cell RAMD32 clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout0 rise@0.000ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        0.382ns  (logic 0.141ns (36.945%)  route 0.241ns (63.055%))
  Logic Levels:           0  
  Clock Path Skew:        0.013ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.030ns
    Source Clock Delay      (SCD):    3.994ns
    Clock Pessimism Removal (CPR):    1.022ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG/O
                         net (fo=4933, routed)        0.565     3.994    sys_clk
    SLICE_X61Y97         FDRE                                         r  soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X61Y97         FDRE (Prop_fdre_C_Q)         0.141     4.135 r  soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/Q
                         net (fo=35, routed)          0.241     4.376    storage_3_reg_0_7_12_17/ADDRD0
    SLICE_X60Y97         RAMD32                                       r  storage_3_reg_0_7_12_17/RAMB_D1/WADR0
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG/O
                         net (fo=4933, routed)        0.836     5.030    storage_3_reg_0_7_12_17/WCLK
    SLICE_X60Y97         RAMD32                                       r  storage_3_reg_0_7_12_17/RAMB_D1/CLK
                         clock pessimism             -1.022     4.007    
    SLICE_X60Y97         RAMD32 (Hold_ramd32_CLK_WADR0)
                                                      0.310     4.317    storage_3_reg_0_7_12_17/RAMB_D1
  -------------------------------------------------------------------
                         required time                         -4.317    
                         arrival time                           4.376    
  -------------------------------------------------------------------
                         slack                                  0.059    

Slack (MET) :             0.059ns  (arrival time - required time)
  Source:                 soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            storage_3_reg_0_7_12_17/RAMC/WADR0
                            (rising edge-triggered cell RAMD32 clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout0 rise@0.000ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        0.382ns  (logic 0.141ns (36.945%)  route 0.241ns (63.055%))
  Logic Levels:           0  
  Clock Path Skew:        0.013ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.030ns
    Source Clock Delay      (SCD):    3.994ns
    Clock Pessimism Removal (CPR):    1.022ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG/O
                         net (fo=4933, routed)        0.565     3.994    sys_clk
    SLICE_X61Y97         FDRE                                         r  soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X61Y97         FDRE (Prop_fdre_C_Q)         0.141     4.135 r  soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/Q
                         net (fo=35, routed)          0.241     4.376    storage_3_reg_0_7_12_17/ADDRD0
    SLICE_X60Y97         RAMD32                                       r  storage_3_reg_0_7_12_17/RAMC/WADR0
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG/O
                         net (fo=4933, routed)        0.836     5.030    storage_3_reg_0_7_12_17/WCLK
    SLICE_X60Y97         RAMD32                                       r  storage_3_reg_0_7_12_17/RAMC/CLK
                         clock pessimism             -1.022     4.007    
    SLICE_X60Y97         RAMD32 (Hold_ramd32_CLK_WADR0)
                                                      0.310     4.317    storage_3_reg_0_7_12_17/RAMC
  -------------------------------------------------------------------
                         required time                         -4.317    
                         arrival time                           4.376    
  -------------------------------------------------------------------
                         slack                                  0.059    

Slack (MET) :             0.059ns  (arrival time - required time)
  Source:                 soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            storage_3_reg_0_7_12_17/RAMC_D1/WADR0
                            (rising edge-triggered cell RAMD32 clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout0 rise@0.000ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        0.382ns  (logic 0.141ns (36.945%)  route 0.241ns (63.055%))
  Logic Levels:           0  
  Clock Path Skew:        0.013ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.030ns
    Source Clock Delay      (SCD):    3.994ns
    Clock Pessimism Removal (CPR):    1.022ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG/O
                         net (fo=4933, routed)        0.565     3.994    sys_clk
    SLICE_X61Y97         FDRE                                         r  soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X61Y97         FDRE (Prop_fdre_C_Q)         0.141     4.135 r  soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/Q
                         net (fo=35, routed)          0.241     4.376    storage_3_reg_0_7_12_17/ADDRD0
    SLICE_X60Y97         RAMD32                                       r  storage_3_reg_0_7_12_17/RAMC_D1/WADR0
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG/O
                         net (fo=4933, routed)        0.836     5.030    storage_3_reg_0_7_12_17/WCLK
    SLICE_X60Y97         RAMD32                                       r  storage_3_reg_0_7_12_17/RAMC_D1/CLK
                         clock pessimism             -1.022     4.007    
    SLICE_X60Y97         RAMD32 (Hold_ramd32_CLK_WADR0)
                                                      0.310     4.317    storage_3_reg_0_7_12_17/RAMC_D1
  -------------------------------------------------------------------
                         required time                         -4.317    
                         arrival time                           4.376    
  -------------------------------------------------------------------
                         slack                                  0.059    

Slack (MET) :             0.059ns  (arrival time - required time)
  Source:                 soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            storage_3_reg_0_7_12_17/RAMD/ADR0
                            (rising edge-triggered cell RAMS32 clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout0 rise@0.000ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        0.382ns  (logic 0.141ns (36.945%)  route 0.241ns (63.055%))
  Logic Levels:           0  
  Clock Path Skew:        0.013ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.030ns
    Source Clock Delay      (SCD):    3.994ns
    Clock Pessimism Removal (CPR):    1.022ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG/O
                         net (fo=4933, routed)        0.565     3.994    sys_clk
    SLICE_X61Y97         FDRE                                         r  soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X61Y97         FDRE (Prop_fdre_C_Q)         0.141     4.135 r  soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/Q
                         net (fo=35, routed)          0.241     4.376    storage_3_reg_0_7_12_17/ADDRD0
    SLICE_X60Y97         RAMS32                                       r  storage_3_reg_0_7_12_17/RAMD/ADR0
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG/O
                         net (fo=4933, routed)        0.836     5.030    storage_3_reg_0_7_12_17/WCLK
    SLICE_X60Y97         RAMS32                                       r  storage_3_reg_0_7_12_17/RAMD/CLK
                         clock pessimism             -1.022     4.007    
    SLICE_X60Y97         RAMS32 (Hold_rams32_CLK_ADR0)
                                                      0.310     4.317    storage_3_reg_0_7_12_17/RAMD
  -------------------------------------------------------------------
                         required time                         -4.317    
                         arrival time                           4.376    
  -------------------------------------------------------------------
                         slack                                  0.059    

Slack (MET) :             0.059ns  (arrival time - required time)
  Source:                 soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Destination:            storage_3_reg_0_7_12_17/RAMD_D1/ADR0
                            (rising edge-triggered cell RAMS32 clocked by soc_crg_clkout0  {rise@0.000ns fall@6.667ns period=13.333ns})
  Path Group:             soc_crg_clkout0
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout0 rise@0.000ns - soc_crg_clkout0 rise@0.000ns)
  Data Path Delay:        0.382ns  (logic 0.141ns (36.945%)  route 0.241ns (63.055%))
  Logic Levels:           0  
  Clock Path Skew:        0.013ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.030ns
    Source Clock Delay      (SCD):    3.994ns
    Clock Pessimism Removal (CPR):    1.022ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG/O
                         net (fo=4933, routed)        0.565     3.994    sys_clk
    SLICE_X61Y97         FDRE                                         r  soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X61Y97         FDRE (Prop_fdre_C_Q)         0.141     4.135 r  soc_basesoc_sdram_bankmachine1_cmd_buffer_lookahead_produce_reg[0]/Q
                         net (fo=35, routed)          0.241     4.376    storage_3_reg_0_7_12_17/ADDRD0
    SLICE_X60Y97         RAMS32                                       r  storage_3_reg_0_7_12_17/RAMD_D1/ADR0
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout0 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT0)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT0
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout0
    BUFGCTRL_X0Y0        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG/O
                         net (fo=4933, routed)        0.836     5.030    storage_3_reg_0_7_12_17/WCLK
    SLICE_X60Y97         RAMS32                                       r  storage_3_reg_0_7_12_17/RAMD_D1/CLK
                         clock pessimism             -1.022     4.007    
    SLICE_X60Y97         RAMS32 (Hold_rams32_CLK_ADR0)
                                                      0.310     4.317    storage_3_reg_0_7_12_17/RAMD_D1
  -------------------------------------------------------------------
                         required time                         -4.317    
                         arrival time                           4.376    
  -------------------------------------------------------------------
                         slack                                  0.059    





Pulse Width Checks
--------------------------------------------------------------------------------------
Clock Name:         soc_crg_clkout0
Waveform(ns):       { 0.000 6.667 }
Period(ns):         13.333
Sources:            { MMCME2_ADV/CLKOUT0 }

Check Type        Corner  Lib Pin             Reference Pin  Required(ns)  Actual(ns)  Slack(ns)  Location         Pin
Min Period        n/a     DSP48E1/CLK         n/a            3.884         13.333      9.449      DSP48_X1Y23      Cfu/fn0/pp/srdhm/ab_reg/CLK
Min Period        n/a     DSP48E1/CLK         n/a            3.687         13.333      9.646      DSP48_X1Y25      Cfu/fn0/pp/srdhm/ab_reg__0/CLK
Min Period        n/a     RAMB18E1/CLKARDCLK  n/a            2.944         13.333      10.389     RAMB18_X1Y24     Cfu/fn0/FIFO/unbuffered/storage_reg/CLKARDCLK
Min Period        n/a     RAMB18E1/CLKBWRCLK  n/a            2.944         13.333      10.389     RAMB18_X1Y24     Cfu/fn0/FIFO/unbuffered/storage_reg/CLKBWRCLK
Min Period        n/a     RAMB36E1/CLKARDCLK  n/a            2.944         13.333      10.389     RAMB36_X1Y6      Cfu/fn0/ins/dp_0/mem_reg/CLKARDCLK
Min Period        n/a     RAMB36E1/CLKARDCLK  n/a            2.944         13.333      10.389     RAMB36_X1Y9      Cfu/fn0/ins/dp_1/mem_reg/CLKARDCLK
Min Period        n/a     RAMB36E1/CLKARDCLK  n/a            2.944         13.333      10.389     RAMB36_X1Y8      Cfu/fn0/ins/dp_2/mem_reg/CLKARDCLK
Min Period        n/a     RAMB36E1/CLKARDCLK  n/a            2.944         13.333      10.389     RAMB36_X1Y7      Cfu/fn0/ins/dp_3/mem_reg/CLKARDCLK
Min Period        n/a     RAMB18E1/CLKARDCLK  n/a            2.944         13.333      10.389     RAMB18_X2Y14     Cfu/fn0/store_filter_values_dp_0/mem_reg/CLKARDCLK
Min Period        n/a     RAMB18E1/CLKBWRCLK  n/a            2.944         13.333      10.389     RAMB18_X2Y14     Cfu/fn0/store_filter_values_dp_0/mem_reg/CLKBWRCLK
Max Period        n/a     MMCME2_ADV/CLKOUT0  n/a            213.360       13.333      200.027    MMCME2_ADV_X0Y0  MMCME2_ADV/CLKOUT0
Low Pulse Width   Slow    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMA/CLK
Low Pulse Width   Fast    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMA/CLK
Low Pulse Width   Slow    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMA_D1/CLK
Low Pulse Width   Fast    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMA_D1/CLK
Low Pulse Width   Slow    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMB/CLK
Low Pulse Width   Fast    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMB/CLK
Low Pulse Width   Slow    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMB_D1/CLK
Low Pulse Width   Fast    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMB_D1/CLK
Low Pulse Width   Slow    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMC/CLK
Low Pulse Width   Fast    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMC/CLK
High Pulse Width  Slow    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMA/CLK
High Pulse Width  Fast    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMA/CLK
High Pulse Width  Slow    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMA_D1/CLK
High Pulse Width  Fast    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMA_D1/CLK
High Pulse Width  Slow    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMB/CLK
High Pulse Width  Fast    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMB/CLK
High Pulse Width  Slow    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMB_D1/CLK
High Pulse Width  Fast    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMB_D1/CLK
High Pulse Width  Slow    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMC/CLK
High Pulse Width  Fast    RAMD32/CLK          n/a            1.250         6.667       5.417      SLICE_X84Y91     storage_1_reg_0_15_0_5/RAMC/CLK



---------------------------------------------------------------------------------------------------
From Clock:  soc_crg_clkout1
  To Clock:  soc_crg_clkout1

Setup :           NA  Failing Endpoints,  Worst Slack           NA  ,  Total Violation           NA
Hold  :           NA  Failing Endpoints,  Worst Slack           NA  ,  Total Violation           NA
PW    :            0  Failing Endpoints,  Worst Slack        4.511ns,  Total Violation        0.000ns
---------------------------------------------------------------------------------------------------


Pulse Width Checks
--------------------------------------------------------------------------------------
Clock Name:         soc_crg_clkout1
Waveform(ns):       { 0.000 3.333 }
Period(ns):         6.667
Sources:            { MMCME2_ADV/CLKOUT1 }

Check Type  Corner  Lib Pin             Reference Pin  Required(ns)  Actual(ns)  Slack(ns)  Location         Pin
Min Period  n/a     BUFG/I              n/a            2.155         6.667       4.511      BUFGCTRL_X0Y1    BUFG_1/I
Min Period  n/a     ISERDESE2/CLK       n/a            1.667         6.667       5.000      ILOGIC_X1Y54     ISERDESE2/CLK
Min Period  n/a     ISERDESE2/CLKB      n/a            1.667         6.667       5.000      ILOGIC_X1Y54     ISERDESE2/CLKB
Min Period  n/a     ISERDESE2/CLK       n/a            1.667         6.667       5.000      ILOGIC_X1Y59     ISERDESE2_1/CLK
Min Period  n/a     ISERDESE2/CLKB      n/a            1.667         6.667       5.000      ILOGIC_X1Y59     ISERDESE2_1/CLKB
Min Period  n/a     ISERDESE2/CLK       n/a            1.667         6.667       5.000      ILOGIC_X1Y80     ISERDESE2_10/CLK
Min Period  n/a     ISERDESE2/CLKB      n/a            1.667         6.667       5.000      ILOGIC_X1Y80     ISERDESE2_10/CLKB
Min Period  n/a     ISERDESE2/CLK       n/a            1.667         6.667       5.000      ILOGIC_X1Y84     ISERDESE2_11/CLK
Min Period  n/a     ISERDESE2/CLKB      n/a            1.667         6.667       5.000      ILOGIC_X1Y84     ISERDESE2_11/CLKB
Min Period  n/a     ISERDESE2/CLK       n/a            1.667         6.667       5.000      ILOGIC_X1Y79     ISERDESE2_12/CLK
Max Period  n/a     MMCME2_ADV/CLKOUT1  n/a            213.360       6.667       206.693    MMCME2_ADV_X0Y0  MMCME2_ADV/CLKOUT1



---------------------------------------------------------------------------------------------------
From Clock:  soc_crg_clkout2
  To Clock:  soc_crg_clkout2

Setup :           NA  Failing Endpoints,  Worst Slack           NA  ,  Total Violation           NA
Hold  :           NA  Failing Endpoints,  Worst Slack           NA  ,  Total Violation           NA
PW    :            0  Failing Endpoints,  Worst Slack        4.511ns,  Total Violation        0.000ns
---------------------------------------------------------------------------------------------------


Pulse Width Checks
--------------------------------------------------------------------------------------
Clock Name:         soc_crg_clkout2
Waveform(ns):       { 1.667 5.000 }
Period(ns):         6.667
Sources:            { MMCME2_ADV/CLKOUT2 }

Check Type  Corner  Lib Pin             Reference Pin  Required(ns)  Actual(ns)  Slack(ns)  Location         Pin
Min Period  n/a     BUFG/I              n/a            2.155         6.667       4.511      BUFGCTRL_X0Y3    BUFG_2/I
Min Period  n/a     OSERDESE2/CLK       n/a            1.667         6.667       5.000      OLOGIC_X1Y58     OSERDESE2_23/CLK
Min Period  n/a     OSERDESE2/CLK       n/a            1.667         6.667       5.000      OLOGIC_X1Y82     OSERDESE2_24/CLK
Min Period  n/a     MMCME2_ADV/CLKOUT2  n/a            1.249         6.667       5.418      MMCME2_ADV_X0Y0  MMCME2_ADV/CLKOUT2
Max Period  n/a     MMCME2_ADV/CLKOUT2  n/a            213.360       6.667       206.693    MMCME2_ADV_X0Y0  MMCME2_ADV/CLKOUT2



---------------------------------------------------------------------------------------------------
From Clock:  soc_crg_clkout3
  To Clock:  soc_crg_clkout3

Setup :            0  Failing Endpoints,  Worst Slack        1.246ns,  Total Violation        0.000ns
Hold  :            0  Failing Endpoints,  Worst Slack        0.122ns,  Total Violation        0.000ns
PW    :            0  Failing Endpoints,  Worst Slack        0.264ns,  Total Violation        0.000ns
---------------------------------------------------------------------------------------------------


Max Delay Paths
--------------------------------------------------------------------------------------
Slack (MET) :             1.246ns  (required time - arrival time)
  Source:                 FDPE_6/C
                            (rising edge-triggered cell FDPE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            FDPE_7/D
                            (rising edge-triggered cell FDPE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            2.000ns  (MaxDelay Path 2.000ns)
  Data Path Delay:        0.646ns  (logic 0.456ns (70.599%)  route 0.190ns (29.401%))
  Logic Levels:           0  
  Clock Path Skew:        0.000ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    11.079ns
    Source Clock Delay      (SCD):    12.040ns
    Clock Pessimism Removal (CPR):    0.962ns
  Clock Uncertainty:      0.061ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.100ns
    Phase Error              (PE):    0.000ns
  Timing Exception:       MaxDelay Path 2.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG_3/O
                         net (fo=8, routed)           1.720    12.040    idelay_clk
    SLICE_X85Y66         FDPE                                         r  FDPE_6/C
  -------------------------------------------------------------------    -------------------
    SLICE_X85Y66         FDPE (Prop_fdpe_C_Q)         0.456    12.496 r  FDPE_6/Q
                         net (fo=1, routed)           0.190    12.686    soc_builder_xilinxasyncresetsynchronizerimpl3_rst_meta
    SLICE_X85Y66         FDPE                                         r  FDPE_7/D
  -------------------------------------------------------------------    -------------------

                         max delay                    2.000     2.000    
    E3                                                0.000     2.000 r  clk100 (IN)
                         net (fo=0)                   0.000     2.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411     3.411 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920     5.331    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091     5.422 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214     7.636    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100     7.736 r  clk100_inst/O
                         net (fo=9, routed)           1.645     9.381    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.083     9.464 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           1.923    11.387    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.091    11.478 r  BUFG_3/O
                         net (fo=8, routed)           1.600    13.079    idelay_clk
    SLICE_X85Y66         FDPE                                         r  FDPE_7/C
                         clock pessimism              0.962    14.040    
                         clock uncertainty           -0.061    13.979    
    SLICE_X85Y66         FDPE (Setup_fdpe_C_D)       -0.047    13.932    FDPE_7
  -------------------------------------------------------------------
                         required time                         13.932    
                         arrival time                         -12.686    
  -------------------------------------------------------------------
                         slack                                  1.246    

Slack (MET) :             2.687ns  (required time - arrival time)
  Source:                 soc_crg_reset_counter_reg[2]/C
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_ic_reset_reg/D
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            5.000ns  (soc_crg_clkout3 rise@5.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        2.259ns  (logic 0.766ns (33.914%)  route 1.493ns (66.086%))
  Logic Levels:           2  (LUT3=1 LUT4=1)
  Clock Path Skew:        -0.022ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    11.078ns = ( 16.078 - 5.000 ) 
    Source Clock Delay      (SCD):    12.039ns
    Clock Pessimism Removal (CPR):    0.940ns
  Clock Uncertainty:      0.061ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.100ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG_3/O
                         net (fo=8, routed)           1.719    12.039    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[2]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X88Y68         FDSE (Prop_fdse_C_Q)         0.518    12.557 r  soc_crg_reset_counter_reg[2]/Q
                         net (fo=3, routed)           0.870    13.428    soc_crg_reset_counter[2]
    SLICE_X88Y68         LUT4 (Prop_lut4_I2_O)        0.124    13.552 r  soc_crg_reset_counter[3]_i_1/O
                         net (fo=5, routed)           0.622    14.174    soc_crg_reset_counter[3]_i_1_n_0
    SLICE_X89Y68         LUT3 (Prop_lut3_I0_O)        0.124    14.298 r  soc_crg_ic_reset_i_1/O
                         net (fo=1, routed)           0.000    14.298    soc_crg_ic_reset_i_1_n_0
    SLICE_X89Y68         FDRE                                         r  soc_crg_ic_reset_reg/D
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      5.000     5.000 r  
    E3                                                0.000     5.000 r  clk100 (IN)
                         net (fo=0)                   0.000     5.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411     6.411 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920     8.331    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091     8.422 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    10.636    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    10.736 r  clk100_inst/O
                         net (fo=9, routed)           1.645    12.381    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.083    12.464 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           1.923    14.387    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.091    14.478 r  BUFG_3/O
                         net (fo=8, routed)           1.599    16.078    idelay_clk
    SLICE_X89Y68         FDRE                                         r  soc_crg_ic_reset_reg/C
                         clock pessimism              0.940    17.017    
                         clock uncertainty           -0.061    16.956    
    SLICE_X89Y68         FDRE (Setup_fdre_C_D)        0.029    16.985    soc_crg_ic_reset_reg
  -------------------------------------------------------------------
                         required time                         16.985    
                         arrival time                         -14.298    
  -------------------------------------------------------------------
                         slack                                  2.687    

Slack (MET) :             2.978ns  (required time - arrival time)
  Source:                 soc_crg_reset_counter_reg[0]/C
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_reset_counter_reg[0]/D
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            5.000ns  (soc_crg_clkout3 rise@5.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        2.038ns  (logic 0.642ns (31.501%)  route 1.396ns (68.499%))
  Logic Levels:           1  (LUT1=1)
  Clock Path Skew:        0.000ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    11.078ns = ( 16.078 - 5.000 ) 
    Source Clock Delay      (SCD):    12.039ns
    Clock Pessimism Removal (CPR):    0.962ns
  Clock Uncertainty:      0.061ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.100ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG_3/O
                         net (fo=8, routed)           1.719    12.039    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X88Y68         FDSE (Prop_fdse_C_Q)         0.518    12.557 f  soc_crg_reset_counter_reg[0]/Q
                         net (fo=5, routed)           1.396    13.953    soc_crg_reset_counter[0]
    SLICE_X88Y68         LUT1 (Prop_lut1_I0_O)        0.124    14.077 r  soc_crg_reset_counter[0]_i_1/O
                         net (fo=1, routed)           0.000    14.077    soc_crg_reset_counter0[0]
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[0]/D
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      5.000     5.000 r  
    E3                                                0.000     5.000 r  clk100 (IN)
                         net (fo=0)                   0.000     5.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411     6.411 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920     8.331    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091     8.422 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    10.636    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    10.736 r  clk100_inst/O
                         net (fo=9, routed)           1.645    12.381    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.083    12.464 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           1.923    14.387    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.091    14.478 r  BUFG_3/O
                         net (fo=8, routed)           1.599    16.078    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[0]/C
                         clock pessimism              0.962    17.039    
                         clock uncertainty           -0.061    16.978    
    SLICE_X88Y68         FDSE (Setup_fdse_C_D)        0.077    17.055    soc_crg_reset_counter_reg[0]
  -------------------------------------------------------------------
                         required time                         17.055    
                         arrival time                         -14.077    
  -------------------------------------------------------------------
                         slack                                  2.978    

Slack (MET) :             2.997ns  (required time - arrival time)
  Source:                 soc_crg_reset_counter_reg[0]/C
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_reset_counter_reg[1]/D
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            5.000ns  (soc_crg_clkout3 rise@5.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        2.060ns  (logic 0.664ns (32.233%)  route 1.396ns (67.767%))
  Logic Levels:           1  (LUT2=1)
  Clock Path Skew:        0.000ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    11.078ns = ( 16.078 - 5.000 ) 
    Source Clock Delay      (SCD):    12.039ns
    Clock Pessimism Removal (CPR):    0.962ns
  Clock Uncertainty:      0.061ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.100ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG_3/O
                         net (fo=8, routed)           1.719    12.039    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X88Y68         FDSE (Prop_fdse_C_Q)         0.518    12.557 r  soc_crg_reset_counter_reg[0]/Q
                         net (fo=5, routed)           1.396    13.953    soc_crg_reset_counter[0]
    SLICE_X88Y68         LUT2 (Prop_lut2_I0_O)        0.146    14.099 r  soc_crg_reset_counter[1]_i_1/O
                         net (fo=1, routed)           0.000    14.099    soc_crg_reset_counter[1]_i_1_n_0
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[1]/D
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      5.000     5.000 r  
    E3                                                0.000     5.000 r  clk100 (IN)
                         net (fo=0)                   0.000     5.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411     6.411 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920     8.331    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091     8.422 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    10.636    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    10.736 r  clk100_inst/O
                         net (fo=9, routed)           1.645    12.381    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.083    12.464 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           1.923    14.387    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.091    14.478 r  BUFG_3/O
                         net (fo=8, routed)           1.599    16.078    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[1]/C
                         clock pessimism              0.962    17.039    
                         clock uncertainty           -0.061    16.978    
    SLICE_X88Y68         FDSE (Setup_fdse_C_D)        0.118    17.096    soc_crg_reset_counter_reg[1]
  -------------------------------------------------------------------
                         required time                         17.096    
                         arrival time                         -14.099    
  -------------------------------------------------------------------
                         slack                                  2.997    

Slack (MET) :             3.067ns  (required time - arrival time)
  Source:                 soc_crg_reset_counter_reg[2]/C
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_reset_counter_reg[0]/CE
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            5.000ns  (soc_crg_clkout3 rise@5.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        1.702ns  (logic 0.642ns (37.716%)  route 1.060ns (62.284%))
  Logic Levels:           1  (LUT4=1)
  Clock Path Skew:        0.000ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    11.078ns = ( 16.078 - 5.000 ) 
    Source Clock Delay      (SCD):    12.039ns
    Clock Pessimism Removal (CPR):    0.962ns
  Clock Uncertainty:      0.061ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.100ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG_3/O
                         net (fo=8, routed)           1.719    12.039    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[2]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X88Y68         FDSE (Prop_fdse_C_Q)         0.518    12.557 r  soc_crg_reset_counter_reg[2]/Q
                         net (fo=3, routed)           0.870    13.428    soc_crg_reset_counter[2]
    SLICE_X88Y68         LUT4 (Prop_lut4_I2_O)        0.124    13.552 r  soc_crg_reset_counter[3]_i_1/O
                         net (fo=5, routed)           0.190    13.742    soc_crg_reset_counter[3]_i_1_n_0
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[0]/CE
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      5.000     5.000 r  
    E3                                                0.000     5.000 r  clk100 (IN)
                         net (fo=0)                   0.000     5.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411     6.411 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920     8.331    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091     8.422 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    10.636    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    10.736 r  clk100_inst/O
                         net (fo=9, routed)           1.645    12.381    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.083    12.464 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           1.923    14.387    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.091    14.478 r  BUFG_3/O
                         net (fo=8, routed)           1.599    16.078    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[0]/C
                         clock pessimism              0.962    17.039    
                         clock uncertainty           -0.061    16.978    
    SLICE_X88Y68         FDSE (Setup_fdse_C_CE)      -0.169    16.809    soc_crg_reset_counter_reg[0]
  -------------------------------------------------------------------
                         required time                         16.809    
                         arrival time                         -13.742    
  -------------------------------------------------------------------
                         slack                                  3.067    

Slack (MET) :             3.067ns  (required time - arrival time)
  Source:                 soc_crg_reset_counter_reg[2]/C
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_reset_counter_reg[1]/CE
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            5.000ns  (soc_crg_clkout3 rise@5.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        1.702ns  (logic 0.642ns (37.716%)  route 1.060ns (62.284%))
  Logic Levels:           1  (LUT4=1)
  Clock Path Skew:        0.000ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    11.078ns = ( 16.078 - 5.000 ) 
    Source Clock Delay      (SCD):    12.039ns
    Clock Pessimism Removal (CPR):    0.962ns
  Clock Uncertainty:      0.061ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.100ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG_3/O
                         net (fo=8, routed)           1.719    12.039    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[2]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X88Y68         FDSE (Prop_fdse_C_Q)         0.518    12.557 r  soc_crg_reset_counter_reg[2]/Q
                         net (fo=3, routed)           0.870    13.428    soc_crg_reset_counter[2]
    SLICE_X88Y68         LUT4 (Prop_lut4_I2_O)        0.124    13.552 r  soc_crg_reset_counter[3]_i_1/O
                         net (fo=5, routed)           0.190    13.742    soc_crg_reset_counter[3]_i_1_n_0
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[1]/CE
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      5.000     5.000 r  
    E3                                                0.000     5.000 r  clk100 (IN)
                         net (fo=0)                   0.000     5.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411     6.411 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920     8.331    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091     8.422 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    10.636    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    10.736 r  clk100_inst/O
                         net (fo=9, routed)           1.645    12.381    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.083    12.464 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           1.923    14.387    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.091    14.478 r  BUFG_3/O
                         net (fo=8, routed)           1.599    16.078    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[1]/C
                         clock pessimism              0.962    17.039    
                         clock uncertainty           -0.061    16.978    
    SLICE_X88Y68         FDSE (Setup_fdse_C_CE)      -0.169    16.809    soc_crg_reset_counter_reg[1]
  -------------------------------------------------------------------
                         required time                         16.809    
                         arrival time                         -13.742    
  -------------------------------------------------------------------
                         slack                                  3.067    

Slack (MET) :             3.067ns  (required time - arrival time)
  Source:                 soc_crg_reset_counter_reg[2]/C
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_reset_counter_reg[2]/CE
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            5.000ns  (soc_crg_clkout3 rise@5.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        1.702ns  (logic 0.642ns (37.716%)  route 1.060ns (62.284%))
  Logic Levels:           1  (LUT4=1)
  Clock Path Skew:        0.000ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    11.078ns = ( 16.078 - 5.000 ) 
    Source Clock Delay      (SCD):    12.039ns
    Clock Pessimism Removal (CPR):    0.962ns
  Clock Uncertainty:      0.061ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.100ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG_3/O
                         net (fo=8, routed)           1.719    12.039    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[2]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X88Y68         FDSE (Prop_fdse_C_Q)         0.518    12.557 r  soc_crg_reset_counter_reg[2]/Q
                         net (fo=3, routed)           0.870    13.428    soc_crg_reset_counter[2]
    SLICE_X88Y68         LUT4 (Prop_lut4_I2_O)        0.124    13.552 r  soc_crg_reset_counter[3]_i_1/O
                         net (fo=5, routed)           0.190    13.742    soc_crg_reset_counter[3]_i_1_n_0
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[2]/CE
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      5.000     5.000 r  
    E3                                                0.000     5.000 r  clk100 (IN)
                         net (fo=0)                   0.000     5.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411     6.411 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920     8.331    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091     8.422 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    10.636    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    10.736 r  clk100_inst/O
                         net (fo=9, routed)           1.645    12.381    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.083    12.464 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           1.923    14.387    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.091    14.478 r  BUFG_3/O
                         net (fo=8, routed)           1.599    16.078    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[2]/C
                         clock pessimism              0.962    17.039    
                         clock uncertainty           -0.061    16.978    
    SLICE_X88Y68         FDSE (Setup_fdse_C_CE)      -0.169    16.809    soc_crg_reset_counter_reg[2]
  -------------------------------------------------------------------
                         required time                         16.809    
                         arrival time                         -13.742    
  -------------------------------------------------------------------
                         slack                                  3.067    

Slack (MET) :             3.067ns  (required time - arrival time)
  Source:                 soc_crg_reset_counter_reg[2]/C
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_reset_counter_reg[3]/CE
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            5.000ns  (soc_crg_clkout3 rise@5.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        1.702ns  (logic 0.642ns (37.716%)  route 1.060ns (62.284%))
  Logic Levels:           1  (LUT4=1)
  Clock Path Skew:        0.000ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    11.078ns = ( 16.078 - 5.000 ) 
    Source Clock Delay      (SCD):    12.039ns
    Clock Pessimism Removal (CPR):    0.962ns
  Clock Uncertainty:      0.061ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.100ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG_3/O
                         net (fo=8, routed)           1.719    12.039    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[2]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X88Y68         FDSE (Prop_fdse_C_Q)         0.518    12.557 r  soc_crg_reset_counter_reg[2]/Q
                         net (fo=3, routed)           0.870    13.428    soc_crg_reset_counter[2]
    SLICE_X88Y68         LUT4 (Prop_lut4_I2_O)        0.124    13.552 r  soc_crg_reset_counter[3]_i_1/O
                         net (fo=5, routed)           0.190    13.742    soc_crg_reset_counter[3]_i_1_n_0
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[3]/CE
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      5.000     5.000 r  
    E3                                                0.000     5.000 r  clk100 (IN)
                         net (fo=0)                   0.000     5.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411     6.411 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920     8.331    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091     8.422 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    10.636    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    10.736 r  clk100_inst/O
                         net (fo=9, routed)           1.645    12.381    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.083    12.464 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           1.923    14.387    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.091    14.478 r  BUFG_3/O
                         net (fo=8, routed)           1.599    16.078    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[3]/C
                         clock pessimism              0.962    17.039    
                         clock uncertainty           -0.061    16.978    
    SLICE_X88Y68         FDSE (Setup_fdse_C_CE)      -0.169    16.809    soc_crg_reset_counter_reg[3]
  -------------------------------------------------------------------
                         required time                         16.809    
                         arrival time                         -13.742    
  -------------------------------------------------------------------
                         slack                                  3.067    

Slack (MET) :             3.124ns  (required time - arrival time)
  Source:                 soc_crg_reset_counter_reg[0]/C
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_reset_counter_reg[2]/D
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            5.000ns  (soc_crg_clkout3 rise@5.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        1.896ns  (logic 0.642ns (33.861%)  route 1.254ns (66.139%))
  Logic Levels:           1  (LUT3=1)
  Clock Path Skew:        0.000ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    11.078ns = ( 16.078 - 5.000 ) 
    Source Clock Delay      (SCD):    12.039ns
    Clock Pessimism Removal (CPR):    0.962ns
  Clock Uncertainty:      0.061ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.100ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG_3/O
                         net (fo=8, routed)           1.719    12.039    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X88Y68         FDSE (Prop_fdse_C_Q)         0.518    12.557 r  soc_crg_reset_counter_reg[0]/Q
                         net (fo=5, routed)           1.254    13.811    soc_crg_reset_counter[0]
    SLICE_X88Y68         LUT3 (Prop_lut3_I1_O)        0.124    13.935 r  soc_crg_reset_counter[2]_i_1/O
                         net (fo=1, routed)           0.000    13.935    soc_crg_reset_counter[2]_i_1_n_0
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[2]/D
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      5.000     5.000 r  
    E3                                                0.000     5.000 r  clk100 (IN)
                         net (fo=0)                   0.000     5.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411     6.411 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920     8.331    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091     8.422 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    10.636    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    10.736 r  clk100_inst/O
                         net (fo=9, routed)           1.645    12.381    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.083    12.464 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           1.923    14.387    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.091    14.478 r  BUFG_3/O
                         net (fo=8, routed)           1.599    16.078    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[2]/C
                         clock pessimism              0.962    17.039    
                         clock uncertainty           -0.061    16.978    
    SLICE_X88Y68         FDSE (Setup_fdse_C_D)        0.081    17.059    soc_crg_reset_counter_reg[2]
  -------------------------------------------------------------------
                         required time                         17.059    
                         arrival time                         -13.935    
  -------------------------------------------------------------------
                         slack                                  3.124    

Slack (MET) :             3.135ns  (required time - arrival time)
  Source:                 soc_crg_reset_counter_reg[0]/C
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_reset_counter_reg[3]/D
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Setup (Max at Slow Process Corner)
  Requirement:            5.000ns  (soc_crg_clkout3 rise@5.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        1.922ns  (logic 0.668ns (34.755%)  route 1.254ns (65.245%))
  Logic Levels:           1  (LUT4=1)
  Clock Path Skew:        0.000ns (DCD - SCD + CPR)
    Destination Clock Delay (DCD):    11.078ns = ( 16.078 - 5.000 ) 
    Source Clock Delay      (SCD):    12.039ns
    Clock Pessimism Removal (CPR):    0.962ns
  Clock Uncertainty:      0.061ns  ((TSJ^2 + DJ^2)^1/2) / 2 + PE
    Total System Jitter     (TSJ):    0.071ns
    Discrete Jitter          (DJ):    0.100ns
    Phase Error              (PE):    0.000ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.482     1.482 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           2.025     3.506    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.096     3.602 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.475     6.077    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.124     6.201 r  clk100_inst/O
                         net (fo=9, routed)           1.916     8.118    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.088     8.206 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           2.018    10.224    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.096    10.320 r  BUFG_3/O
                         net (fo=8, routed)           1.719    12.039    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[0]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X88Y68         FDSE (Prop_fdse_C_Q)         0.518    12.557 r  soc_crg_reset_counter_reg[0]/Q
                         net (fo=5, routed)           1.254    13.811    soc_crg_reset_counter[0]
    SLICE_X88Y68         LUT4 (Prop_lut4_I1_O)        0.150    13.961 r  soc_crg_reset_counter[3]_i_2/O
                         net (fo=1, routed)           0.000    13.961    soc_crg_reset_counter[3]_i_2_n_0
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[3]/D
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      5.000     5.000 r  
    E3                                                0.000     5.000 r  clk100 (IN)
                         net (fo=0)                   0.000     5.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         1.411     6.411 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           1.920     8.331    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.091     8.422 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           2.214    10.636    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.100    10.736 r  clk100_inst/O
                         net (fo=9, routed)           1.645    12.381    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.083    12.464 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           1.923    14.387    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.091    14.478 r  BUFG_3/O
                         net (fo=8, routed)           1.599    16.078    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[3]/C
                         clock pessimism              0.962    17.039    
                         clock uncertainty           -0.061    16.978    
    SLICE_X88Y68         FDSE (Setup_fdse_C_D)        0.118    17.096    soc_crg_reset_counter_reg[3]
  -------------------------------------------------------------------
                         required time                         17.096    
                         arrival time                         -13.961    
  -------------------------------------------------------------------
                         slack                                  3.135    





Min Delay Paths
--------------------------------------------------------------------------------------
Slack (MET) :             0.122ns  (arrival time - required time)
  Source:                 FDPE_6/C
                            (rising edge-triggered cell FDPE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            FDPE_7/D
                            (rising edge-triggered cell FDPE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout3 rise@0.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        0.197ns  (logic 0.141ns (71.611%)  route 0.056ns (28.389%))
  Logic Levels:           0  
  Clock Path Skew:        0.000ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.063ns
    Source Clock Delay      (SCD):    4.028ns
    Clock Pessimism Removal (CPR):    1.034ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG_3/O
                         net (fo=8, routed)           0.599     4.028    idelay_clk
    SLICE_X85Y66         FDPE                                         r  FDPE_6/C
  -------------------------------------------------------------------    -------------------
    SLICE_X85Y66         FDPE (Prop_fdpe_C_Q)         0.141     4.169 r  FDPE_6/Q
                         net (fo=1, routed)           0.056     4.225    soc_builder_xilinxasyncresetsynchronizerimpl3_rst_meta
    SLICE_X85Y66         FDPE                                         r  FDPE_7/D
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG_3/O
                         net (fo=8, routed)           0.869     5.063    idelay_clk
    SLICE_X85Y66         FDPE                                         r  FDPE_7/C
                         clock pessimism             -1.034     4.028    
    SLICE_X85Y66         FDPE (Hold_fdpe_C_D)         0.075     4.103    FDPE_7
  -------------------------------------------------------------------
                         required time                         -4.103    
                         arrival time                           4.225    
  -------------------------------------------------------------------
                         slack                                  0.122    

Slack (MET) :             0.265ns  (arrival time - required time)
  Source:                 soc_crg_ic_reset_reg/C
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_ic_reset_reg/D
                            (rising edge-triggered cell FDRE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout3 rise@0.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        0.356ns  (logic 0.186ns (52.178%)  route 0.170ns (47.822%))
  Logic Levels:           1  (LUT3=1)
  Clock Path Skew:        0.000ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.062ns
    Source Clock Delay      (SCD):    4.027ns
    Clock Pessimism Removal (CPR):    1.034ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG_3/O
                         net (fo=8, routed)           0.598     4.027    idelay_clk
    SLICE_X89Y68         FDRE                                         r  soc_crg_ic_reset_reg/C
  -------------------------------------------------------------------    -------------------
    SLICE_X89Y68         FDRE (Prop_fdre_C_Q)         0.141     4.168 r  soc_crg_ic_reset_reg/Q
                         net (fo=2, routed)           0.170     4.339    soc_crg_ic_reset
    SLICE_X89Y68         LUT3 (Prop_lut3_I1_O)        0.045     4.384 r  soc_crg_ic_reset_i_1/O
                         net (fo=1, routed)           0.000     4.384    soc_crg_ic_reset_i_1_n_0
    SLICE_X89Y68         FDRE                                         r  soc_crg_ic_reset_reg/D
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG_3/O
                         net (fo=8, routed)           0.868     5.062    idelay_clk
    SLICE_X89Y68         FDRE                                         r  soc_crg_ic_reset_reg/C
                         clock pessimism             -1.034     4.027    
    SLICE_X89Y68         FDRE (Hold_fdre_C_D)         0.091     4.118    soc_crg_ic_reset_reg
  -------------------------------------------------------------------
                         required time                         -4.118    
                         arrival time                           4.384    
  -------------------------------------------------------------------
                         slack                                  0.265    

Slack (MET) :             0.289ns  (arrival time - required time)
  Source:                 soc_crg_reset_counter_reg[1]/C
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_reset_counter_reg[1]/D
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout3 rise@0.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        0.420ns  (logic 0.249ns (59.298%)  route 0.171ns (40.702%))
  Logic Levels:           1  (LUT2=1)
  Clock Path Skew:        0.000ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.062ns
    Source Clock Delay      (SCD):    4.027ns
    Clock Pessimism Removal (CPR):    1.034ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG_3/O
                         net (fo=8, routed)           0.598     4.027    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[1]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X88Y68         FDSE (Prop_fdse_C_Q)         0.148     4.175 r  soc_crg_reset_counter_reg[1]/Q
                         net (fo=4, routed)           0.171     4.346    soc_crg_reset_counter[1]
    SLICE_X88Y68         LUT2 (Prop_lut2_I1_O)        0.101     4.447 r  soc_crg_reset_counter[1]_i_1/O
                         net (fo=1, routed)           0.000     4.447    soc_crg_reset_counter[1]_i_1_n_0
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[1]/D
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG_3/O
                         net (fo=8, routed)           0.868     5.062    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[1]/C
                         clock pessimism             -1.034     4.027    
    SLICE_X88Y68         FDSE (Hold_fdse_C_D)         0.131     4.158    soc_crg_reset_counter_reg[1]
  -------------------------------------------------------------------
                         required time                         -4.158    
                         arrival time                           4.447    
  -------------------------------------------------------------------
                         slack                                  0.289    

Slack (MET) :             0.293ns  (arrival time - required time)
  Source:                 soc_crg_reset_counter_reg[1]/C
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_reset_counter_reg[3]/D
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout3 rise@0.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        0.424ns  (logic 0.249ns (58.739%)  route 0.175ns (41.261%))
  Logic Levels:           1  (LUT4=1)
  Clock Path Skew:        0.000ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.062ns
    Source Clock Delay      (SCD):    4.027ns
    Clock Pessimism Removal (CPR):    1.034ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG_3/O
                         net (fo=8, routed)           0.598     4.027    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[1]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X88Y68         FDSE (Prop_fdse_C_Q)         0.148     4.175 r  soc_crg_reset_counter_reg[1]/Q
                         net (fo=4, routed)           0.175     4.350    soc_crg_reset_counter[1]
    SLICE_X88Y68         LUT4 (Prop_lut4_I2_O)        0.101     4.451 r  soc_crg_reset_counter[3]_i_2/O
                         net (fo=1, routed)           0.000     4.451    soc_crg_reset_counter[3]_i_2_n_0
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[3]/D
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG_3/O
                         net (fo=8, routed)           0.868     5.062    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[3]/C
                         clock pessimism             -1.034     4.027    
    SLICE_X88Y68         FDSE (Hold_fdse_C_D)         0.131     4.158    soc_crg_reset_counter_reg[3]
  -------------------------------------------------------------------
                         required time                         -4.158    
                         arrival time                           4.451    
  -------------------------------------------------------------------
                         slack                                  0.293    

Slack (MET) :             0.300ns  (arrival time - required time)
  Source:                 soc_crg_reset_counter_reg[1]/C
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_reset_counter_reg[2]/D
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout3 rise@0.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        0.421ns  (logic 0.246ns (58.445%)  route 0.175ns (41.555%))
  Logic Levels:           1  (LUT3=1)
  Clock Path Skew:        0.000ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.062ns
    Source Clock Delay      (SCD):    4.027ns
    Clock Pessimism Removal (CPR):    1.034ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG_3/O
                         net (fo=8, routed)           0.598     4.027    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[1]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X88Y68         FDSE (Prop_fdse_C_Q)         0.148     4.175 r  soc_crg_reset_counter_reg[1]/Q
                         net (fo=4, routed)           0.175     4.350    soc_crg_reset_counter[1]
    SLICE_X88Y68         LUT3 (Prop_lut3_I0_O)        0.098     4.448 r  soc_crg_reset_counter[2]_i_1/O
                         net (fo=1, routed)           0.000     4.448    soc_crg_reset_counter[2]_i_1_n_0
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[2]/D
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG_3/O
                         net (fo=8, routed)           0.868     5.062    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[2]/C
                         clock pessimism             -1.034     4.027    
    SLICE_X88Y68         FDSE (Hold_fdse_C_D)         0.121     4.148    soc_crg_reset_counter_reg[2]
  -------------------------------------------------------------------
                         required time                         -4.148    
                         arrival time                           4.448    
  -------------------------------------------------------------------
                         slack                                  0.300    

Slack (MET) :             0.383ns  (arrival time - required time)
  Source:                 FDPE_7/C
                            (rising edge-triggered cell FDPE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_reset_counter_reg[0]/S
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout3 rise@0.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        0.373ns  (logic 0.128ns (34.288%)  route 0.245ns (65.712%))
  Logic Levels:           0  
  Clock Path Skew:        0.035ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.062ns
    Source Clock Delay      (SCD):    4.028ns
    Clock Pessimism Removal (CPR):    0.998ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG_3/O
                         net (fo=8, routed)           0.599     4.028    idelay_clk
    SLICE_X85Y66         FDPE                                         r  FDPE_7/C
  -------------------------------------------------------------------    -------------------
    SLICE_X85Y66         FDPE (Prop_fdpe_C_Q)         0.128     4.156 r  FDPE_7/Q
                         net (fo=5, routed)           0.245     4.402    idelay_rst
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[0]/S
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG_3/O
                         net (fo=8, routed)           0.868     5.062    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[0]/C
                         clock pessimism             -0.998     4.063    
    SLICE_X88Y68         FDSE (Hold_fdse_C_S)        -0.045     4.018    soc_crg_reset_counter_reg[0]
  -------------------------------------------------------------------
                         required time                         -4.018    
                         arrival time                           4.402    
  -------------------------------------------------------------------
                         slack                                  0.383    

Slack (MET) :             0.383ns  (arrival time - required time)
  Source:                 FDPE_7/C
                            (rising edge-triggered cell FDPE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_reset_counter_reg[1]/S
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout3 rise@0.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        0.373ns  (logic 0.128ns (34.288%)  route 0.245ns (65.712%))
  Logic Levels:           0  
  Clock Path Skew:        0.035ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.062ns
    Source Clock Delay      (SCD):    4.028ns
    Clock Pessimism Removal (CPR):    0.998ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG_3/O
                         net (fo=8, routed)           0.599     4.028    idelay_clk
    SLICE_X85Y66         FDPE                                         r  FDPE_7/C
  -------------------------------------------------------------------    -------------------
    SLICE_X85Y66         FDPE (Prop_fdpe_C_Q)         0.128     4.156 r  FDPE_7/Q
                         net (fo=5, routed)           0.245     4.402    idelay_rst
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[1]/S
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG_3/O
                         net (fo=8, routed)           0.868     5.062    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[1]/C
                         clock pessimism             -0.998     4.063    
    SLICE_X88Y68         FDSE (Hold_fdse_C_S)        -0.045     4.018    soc_crg_reset_counter_reg[1]
  -------------------------------------------------------------------
                         required time                         -4.018    
                         arrival time                           4.402    
  -------------------------------------------------------------------
                         slack                                  0.383    

Slack (MET) :             0.383ns  (arrival time - required time)
  Source:                 FDPE_7/C
                            (rising edge-triggered cell FDPE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_reset_counter_reg[2]/S
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout3 rise@0.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        0.373ns  (logic 0.128ns (34.288%)  route 0.245ns (65.712%))
  Logic Levels:           0  
  Clock Path Skew:        0.035ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.062ns
    Source Clock Delay      (SCD):    4.028ns
    Clock Pessimism Removal (CPR):    0.998ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG_3/O
                         net (fo=8, routed)           0.599     4.028    idelay_clk
    SLICE_X85Y66         FDPE                                         r  FDPE_7/C
  -------------------------------------------------------------------    -------------------
    SLICE_X85Y66         FDPE (Prop_fdpe_C_Q)         0.128     4.156 r  FDPE_7/Q
                         net (fo=5, routed)           0.245     4.402    idelay_rst
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[2]/S
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG_3/O
                         net (fo=8, routed)           0.868     5.062    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[2]/C
                         clock pessimism             -0.998     4.063    
    SLICE_X88Y68         FDSE (Hold_fdse_C_S)        -0.045     4.018    soc_crg_reset_counter_reg[2]
  -------------------------------------------------------------------
                         required time                         -4.018    
                         arrival time                           4.402    
  -------------------------------------------------------------------
                         slack                                  0.383    

Slack (MET) :             0.383ns  (arrival time - required time)
  Source:                 FDPE_7/C
                            (rising edge-triggered cell FDPE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_reset_counter_reg[3]/S
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout3 rise@0.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        0.373ns  (logic 0.128ns (34.288%)  route 0.245ns (65.712%))
  Logic Levels:           0  
  Clock Path Skew:        0.035ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.062ns
    Source Clock Delay      (SCD):    4.028ns
    Clock Pessimism Removal (CPR):    0.998ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG_3/O
                         net (fo=8, routed)           0.599     4.028    idelay_clk
    SLICE_X85Y66         FDPE                                         r  FDPE_7/C
  -------------------------------------------------------------------    -------------------
    SLICE_X85Y66         FDPE (Prop_fdpe_C_Q)         0.128     4.156 r  FDPE_7/Q
                         net (fo=5, routed)           0.245     4.402    idelay_rst
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[3]/S
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG_3/O
                         net (fo=8, routed)           0.868     5.062    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[3]/C
                         clock pessimism             -0.998     4.063    
    SLICE_X88Y68         FDSE (Hold_fdse_C_S)        -0.045     4.018    soc_crg_reset_counter_reg[3]
  -------------------------------------------------------------------
                         required time                         -4.018    
                         arrival time                           4.402    
  -------------------------------------------------------------------
                         slack                                  0.383    

Slack (MET) :             0.426ns  (arrival time - required time)
  Source:                 soc_crg_reset_counter_reg[3]/C
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Destination:            soc_crg_reset_counter_reg[0]/CE
                            (rising edge-triggered cell FDSE clocked by soc_crg_clkout3  {rise@0.000ns fall@2.500ns period=5.000ns})
  Path Group:             soc_crg_clkout3
  Path Type:              Hold (Min at Fast Process Corner)
  Requirement:            0.000ns  (soc_crg_clkout3 rise@0.000ns - soc_crg_clkout3 rise@0.000ns)
  Data Path Delay:        0.410ns  (logic 0.247ns (60.211%)  route 0.163ns (39.789%))
  Logic Levels:           1  (LUT4=1)
  Clock Path Skew:        0.000ns (DCD - SCD - CPR)
    Destination Clock Delay (DCD):    5.062ns
    Source Clock Delay      (SCD):    4.027ns
    Clock Pessimism Removal (CPR):    1.034ns

    Location             Delay type                Incr(ns)  Path(ns)    Netlist Resource(s)
  -------------------------------------------------------------------    -------------------
                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.250     0.250 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.644     0.894    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.026     0.920 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           0.856     1.776    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.045     1.821 r  clk100_inst/O
                         net (fo=9, routed)           0.885     2.706    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.050     2.756 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.648     3.404    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.026     3.430 r  BUFG_3/O
                         net (fo=8, routed)           0.598     4.027    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[3]/C
  -------------------------------------------------------------------    -------------------
    SLICE_X88Y68         FDSE (Prop_fdse_C_Q)         0.148     4.175 r  soc_crg_reset_counter_reg[3]/Q
                         net (fo=2, routed)           0.108     4.283    soc_crg_reset_counter[3]
    SLICE_X88Y68         LUT4 (Prop_lut4_I3_O)        0.099     4.382 r  soc_crg_reset_counter[3]_i_1/O
                         net (fo=5, routed)           0.056     4.437    soc_crg_reset_counter[3]_i_1_n_0
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[0]/CE
  -------------------------------------------------------------------    -------------------

                         (clock soc_crg_clkout3 rise edge)
                                                      0.000     0.000 r  
    E3                                                0.000     0.000 r  clk100 (IN)
                         net (fo=0)                   0.000     0.000    clk100
    E3                   IBUF (Prop_ibuf_I_O)         0.438     0.438 r  clk100_IBUF_inst/O
                         net (fo=1, routed)           0.699     1.136    clk100_IBUF
    BUFGCTRL_X0Y16       BUFG (Prop_bufg_I_O)         0.029     1.165 r  clk100_IBUF_BUFG_inst/O
                         net (fo=1, routed)           1.181     2.347    clk100_IBUF_BUFG
    SLICE_X40Y35         LUT1 (Prop_lut1_I0_O)        0.056     2.403 r  clk100_inst/O
                         net (fo=9, routed)           1.009     3.412    soc_crg_clkin
    MMCME2_ADV_X0Y0      MMCME2_ADV (Prop_mmcme2_adv_CLKIN1_CLKOUT3)
                                                      0.053     3.465 r  MMCME2_ADV/CLKOUT3
                         net (fo=1, routed)           0.700     4.165    soc_crg_clkout3
    BUFGCTRL_X0Y2        BUFG (Prop_bufg_I_O)         0.029     4.194 r  BUFG_3/O
                         net (fo=8, routed)           0.868     5.062    idelay_clk
    SLICE_X88Y68         FDSE                                         r  soc_crg_reset_counter_reg[0]/C
                         clock pessimism             -1.034     4.027    
    SLICE_X88Y68         FDSE (Hold_fdse_C_CE)       -0.016     4.011    soc_crg_reset_counter_reg[0]
  -------------------------------------------------------------------
                         required time                         -4.011    
                         arrival time                           4.437    
  -------------------------------------------------------------------
                         slack                                  0.426    





Pulse Width Checks
--------------------------------------------------------------------------------------
Clock Name:         soc_crg_clkout3
Waveform(ns):       { 0.000 2.500 }
Period(ns):         5.000
Sources:            { MMCME2_ADV/CLKOUT3 }

Check Type        Corner  Lib Pin             Reference Pin  Required(ns)  Actual(ns)  Slack(ns)  Location         Pin
Min Period        n/a     IDELAYCTRL/REFCLK   n/a            3.225         5.000       1.775      IDELAYCTRL_X1Y1  IDELAYCTRL/REFCLK
Min Period        n/a     BUFG/I              n/a            2.155         5.000       2.845      BUFGCTRL_X0Y2    BUFG_3/I
Min Period        n/a     MMCME2_ADV/CLKOUT3  n/a            1.249         5.000       3.751      MMCME2_ADV_X0Y0  MMCME2_ADV/CLKOUT3
Min Period        n/a     FDPE/C              n/a            1.000         5.000       4.000      SLICE_X85Y66     FDPE_6/C
Min Period        n/a     FDPE/C              n/a            1.000         5.000       4.000      SLICE_X85Y66     FDPE_7/C
Min Period        n/a     FDRE/C              n/a            1.000         5.000       4.000      SLICE_X89Y68     soc_crg_ic_reset_reg/C
Min Period        n/a     FDSE/C              n/a            1.000         5.000       4.000      SLICE_X88Y68     soc_crg_reset_counter_reg[0]/C
Min Period        n/a     FDSE/C              n/a            1.000         5.000       4.000      SLICE_X88Y68     soc_crg_reset_counter_reg[1]/C
Min Period        n/a     FDSE/C              n/a            1.000         5.000       4.000      SLICE_X88Y68     soc_crg_reset_counter_reg[2]/C
Min Period        n/a     FDSE/C              n/a            1.000         5.000       4.000      SLICE_X88Y68     soc_crg_reset_counter_reg[3]/C
Max Period        n/a     IDELAYCTRL/REFCLK   n/a            5.264         5.000       0.264      IDELAYCTRL_X1Y1  IDELAYCTRL/REFCLK
Max Period        n/a     MMCME2_ADV/CLKOUT3  n/a            213.360       5.000       208.360    MMCME2_ADV_X0Y0  MMCME2_ADV/CLKOUT3
Low Pulse Width   Slow    FDPE/C              n/a            0.500         2.500       2.000      SLICE_X85Y66     FDPE_6/C
Low Pulse Width   Fast    FDPE/C              n/a            0.500         2.500       2.000      SLICE_X85Y66     FDPE_6/C
Low Pulse Width   Slow    FDPE/C              n/a            0.500         2.500       2.000      SLICE_X85Y66     FDPE_7/C
Low Pulse Width   Fast    FDPE/C              n/a            0.500         2.500       2.000      SLICE_X85Y66     FDPE_7/C
Low Pulse Width   Slow    FDRE/C              n/a            0.500         2.500       2.000      SLICE_X89Y68     soc_crg_ic_reset_reg/C
Low Pulse Width   Fast    FDRE/C              n/a            0.500         2.500       2.000      SLICE_X89Y68     soc_crg_ic_reset_reg/C
Low Pulse Width   Slow    FDSE/C              n/a            0.500         2.500       2.000      SLICE_X88Y68     soc_crg_reset_counter_reg[0]/C
Low Pulse Width   Fast    FDSE/C              n/a            0.500         2.500       2.000      SLICE_X88Y68     soc_crg_reset_counter_reg[0]/C
Low Pulse Width   Slow    FDSE/C              n/a            0.500         2.500       2.000      SLICE_X88Y68     soc_crg_reset_counter_reg[1]/C
Low Pulse Width   Fast    FDSE/C              n/a            0.500         2.500       2.000      SLICE_X88Y68     soc_crg_reset_counter_reg[1]/C
High Pulse Width  Slow    FDPE/C              n/a            0.500         2.500       2.000      SLICE_X85Y66     FDPE_6/C
High Pulse Width  Fast    FDPE/C              n/a            0.500         2.500       2.000      SLICE_X85Y66     FDPE_6/C
High Pulse Width  Slow    FDPE/C              n/a            0.500         2.500       2.000      SLICE_X85Y66     FDPE_7/C
High Pulse Width  Fast    FDPE/C              n/a            0.500         2.500       2.000      SLICE_X85Y66     FDPE_7/C
High Pulse Width  Slow    FDRE/C              n/a            0.500         2.500       2.000      SLICE_X89Y68     soc_crg_ic_reset_reg/C
High Pulse Width  Fast    FDRE/C              n/a            0.500         2.500       2.000      SLICE_X89Y68     soc_crg_ic_reset_reg/C
High Pulse Width  Slow    FDSE/C              n/a            0.500         2.500       2.000      SLICE_X88Y68     soc_crg_reset_counter_reg[0]/C
High Pulse Width  Fast    FDSE/C              n/a            0.500         2.500       2.000      SLICE_X88Y68     soc_crg_reset_counter_reg[0]/C
High Pulse Width  Slow    FDSE/C              n/a            0.500         2.500       2.000      SLICE_X88Y68     soc_crg_reset_counter_reg[1]/C
High Pulse Width  Fast    FDSE/C              n/a            0.500         2.500       2.000      SLICE_X88Y68     soc_crg_reset_counter_reg[1]/C



------------------------------------------------------------------------------------------------
| Data sheet
| ----------
------------------------------------------------------------------------------------------------

Input Ports Setup/Hold

----------+--------------+----------------+----------+---------------+---------+---------------+---------+-----------------+
Reference | Input        | IO Reg         | Delay    |     Setup(ns) | Process |      Hold(ns) | Process | Internal        |
Clock     | Port         | Type           | Type     | to Clk (Edge) | Corner  | to Clk (Edge) | Corner  | Clock           |
----------+--------------+----------------+----------+---------------+---------+---------------+---------+-----------------+
clk100    | cpu_reset    | FDCE           | -        |    -0.099 (r) | FAST    |     3.766 (r) | SLOW    |                 |
clk100    | serial_rx    | FDRE           | -        |    -2.340 (r) | FAST    |     9.014 (r) | SLOW    | soc_crg_clkout0 |
clk100    | ddram_dq[0]  | ISERDESE2 (IO) | VARIABLE |    -3.185 (r) | FAST    |    10.595 (r) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[0]  | ISERDESE2 (IO) | VARIABLE |    -3.113 (f) | FAST    |    10.595 (f) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[1]  | ISERDESE2 (IO) | VARIABLE |    -3.184 (r) | FAST    |    10.592 (r) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[1]  | ISERDESE2 (IO) | VARIABLE |    -3.112 (f) | FAST    |    10.592 (f) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[2]  | ISERDESE2 (IO) | VARIABLE |    -3.201 (r) | FAST    |    10.611 (r) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[2]  | ISERDESE2 (IO) | VARIABLE |    -3.129 (f) | FAST    |    10.611 (f) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[3]  | ISERDESE2 (IO) | VARIABLE |    -3.184 (r) | FAST    |    10.594 (r) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[3]  | ISERDESE2 (IO) | VARIABLE |    -3.112 (f) | FAST    |    10.594 (f) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[4]  | ISERDESE2 (IO) | VARIABLE |    -3.178 (r) | FAST    |    10.586 (r) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[4]  | ISERDESE2 (IO) | VARIABLE |    -3.106 (f) | FAST    |    10.586 (f) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[5]  | ISERDESE2 (IO) | VARIABLE |    -3.193 (r) | FAST    |    10.601 (r) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[5]  | ISERDESE2 (IO) | VARIABLE |    -3.121 (f) | FAST    |    10.601 (f) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[6]  | ISERDESE2 (IO) | VARIABLE |    -3.180 (r) | FAST    |    10.590 (r) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[6]  | ISERDESE2 (IO) | VARIABLE |    -3.108 (f) | FAST    |    10.590 (f) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[7]  | ISERDESE2 (IO) | VARIABLE |    -3.202 (r) | FAST    |    10.611 (r) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[7]  | ISERDESE2 (IO) | VARIABLE |    -3.130 (f) | FAST    |    10.611 (f) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[8]  | ISERDESE2 (IO) | VARIABLE |    -3.179 (r) | FAST    |    10.581 (r) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[8]  | ISERDESE2 (IO) | VARIABLE |    -3.107 (f) | FAST    |    10.581 (f) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[9]  | ISERDESE2 (IO) | VARIABLE |    -3.170 (r) | FAST    |    10.577 (r) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[9]  | ISERDESE2 (IO) | VARIABLE |    -3.098 (f) | FAST    |    10.577 (f) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[10] | ISERDESE2 (IO) | VARIABLE |    -3.172 (r) | FAST    |    10.575 (r) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[10] | ISERDESE2 (IO) | VARIABLE |    -3.100 (f) | FAST    |    10.575 (f) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[11] | ISERDESE2 (IO) | VARIABLE |    -3.165 (r) | FAST    |    10.572 (r) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[11] | ISERDESE2 (IO) | VARIABLE |    -3.093 (f) | FAST    |    10.572 (f) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[12] | ISERDESE2 (IO) | VARIABLE |    -3.161 (r) | FAST    |    10.564 (r) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[12] | ISERDESE2 (IO) | VARIABLE |    -3.089 (f) | FAST    |    10.564 (f) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[13] | ISERDESE2 (IO) | VARIABLE |    -3.184 (r) | FAST    |    10.586 (r) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[13] | ISERDESE2 (IO) | VARIABLE |    -3.112 (f) | FAST    |    10.586 (f) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[14] | ISERDESE2 (IO) | VARIABLE |    -3.172 (r) | FAST    |    10.580 (r) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[14] | ISERDESE2 (IO) | VARIABLE |    -3.100 (f) | FAST    |    10.580 (f) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[15] | ISERDESE2 (IO) | VARIABLE |    -3.185 (r) | FAST    |    10.588 (r) | SLOW    | soc_crg_clkout1 |
clk100    | ddram_dq[15] | ISERDESE2 (IO) | VARIABLE |    -3.113 (f) | FAST    |    10.588 (f) | SLOW    | soc_crg_clkout1 |
----------+--------------+----------------+----------+---------------+---------+---------------+---------+-----------------+


Output Ports Clock-to-out

----------+----------------+----------------+-------+----------------+---------+----------------+---------+-----------------+
Reference | Output         | IO Reg         | Delay | Max Clk (Edge) | Process | Min Clk (Edge) | Process | Internal        |
Clock     | Port           | Type           | Type  |    to port(ns) | Corner  |    to port(ns) | Corner  | Clock           |
----------+----------------+----------------+-------+----------------+---------+----------------+---------+-----------------+
clk100    | ddram_dq[0]    | FDRE           | -     |     18.737 (r) | SLOW    |      5.772 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dq[1]    | FDRE           | -     |     18.272 (r) | SLOW    |      5.575 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dq[2]    | FDRE           | -     |     18.877 (r) | SLOW    |      5.815 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dq[3]    | FDRE           | -     |     18.713 (r) | SLOW    |      5.767 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dq[4]    | FDRE           | -     |     18.122 (r) | SLOW    |      5.518 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dq[5]    | FDRE           | -     |     18.112 (r) | SLOW    |      5.495 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dq[6]    | FDRE           | -     |     18.573 (r) | SLOW    |      5.716 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dq[7]    | FDRE           | -     |     17.972 (r) | SLOW    |      5.431 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dq[8]    | FDRE           | -     |     17.515 (r) | SLOW    |      5.223 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dq[9]    | FDRE           | -     |     17.213 (r) | SLOW    |      5.127 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dq[10]   | FDRE           | -     |     16.920 (r) | SLOW    |      4.998 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dq[11]   | FDRE           | -     |     17.363 (r) | SLOW    |      5.197 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dq[12]   | FDRE           | -     |     16.909 (r) | SLOW    |      5.012 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dq[13]   | FDRE           | -     |     17.375 (r) | SLOW    |      5.163 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dq[14]   | FDRE           | -     |     17.503 (r) | SLOW    |      5.245 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dq[15]   | FDRE           | -     |     17.213 (r) | SLOW    |      5.083 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dqs_n[0] | FDRE           | -     |     18.034 (r) | SLOW    |      5.470 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dqs_n[1] | FDRE           | -     |     17.188 (r) | SLOW    |      5.097 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dqs_p[0] | FDRE           | -     |     18.035 (r) | SLOW    |      5.472 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_dqs_p[1] | FDRE           | -     |     17.189 (r) | SLOW    |      5.097 (r) | FAST    | soc_crg_clkout0 |
clk100    | serial_tx      | FDSE           | -     |     18.839 (r) | SLOW    |      6.009 (r) | FAST    | soc_crg_clkout0 |
clk100    | user_led0      | FDRE           | -     |     22.298 (r) | SLOW    |      7.179 (r) | FAST    | soc_crg_clkout0 |
clk100    | user_led1      | FDRE           | -     |     22.674 (r) | SLOW    |      7.098 (r) | FAST    | soc_crg_clkout0 |
clk100    | user_led10     | FDRE           | -     |     22.977 (r) | SLOW    |      7.589 (r) | FAST    | soc_crg_clkout0 |
clk100    | user_led11     | FDRE           | -     |     22.197 (r) | SLOW    |      7.373 (r) | FAST    | soc_crg_clkout0 |
clk100    | user_led12     | FDRE           | -     |     22.717 (r) | SLOW    |      7.552 (r) | FAST    | soc_crg_clkout0 |
clk100    | user_led13     | FDRE           | -     |     22.726 (r) | SLOW    |      7.740 (r) | FAST    | soc_crg_clkout0 |
clk100    | user_led14     | FDRE           | -     |     22.760 (r) | SLOW    |      7.768 (r) | FAST    | soc_crg_clkout0 |
clk100    | user_led15     | FDRE           | -     |     22.723 (r) | SLOW    |      7.657 (r) | FAST    | soc_crg_clkout0 |
clk100    | user_led2      | FDRE           | -     |     23.200 (r) | SLOW    |      7.266 (r) | FAST    | soc_crg_clkout0 |
clk100    | user_led3      | FDRE           | -     |     21.909 (r) | SLOW    |      6.896 (r) | FAST    | soc_crg_clkout0 |
clk100    | user_led4      | FDRE           | -     |     22.564 (r) | SLOW    |      7.095 (r) | FAST    | soc_crg_clkout0 |
clk100    | user_led5      | FDRE           | -     |     23.186 (r) | SLOW    |      7.343 (r) | FAST    | soc_crg_clkout0 |
clk100    | user_led6      | FDRE           | -     |     22.363 (r) | SLOW    |      6.901 (r) | FAST    | soc_crg_clkout0 |
clk100    | user_led7      | FDRE           | -     |     22.660 (r) | SLOW    |      7.533 (r) | FAST    | soc_crg_clkout0 |
clk100    | user_led8      | FDRE           | -     |     21.720 (r) | SLOW    |      6.955 (r) | FAST    | soc_crg_clkout0 |
clk100    | user_led9      | FDRE           | -     |     22.144 (r) | SLOW    |      6.990 (r) | FAST    | soc_crg_clkout0 |
clk100    | ddram_a[0]     | OSERDESE2 (IO) | -     |     14.204 (r) | SLOW    |      4.566 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_a[1]     | OSERDESE2 (IO) | -     |     14.219 (r) | SLOW    |      4.583 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_a[2]     | OSERDESE2 (IO) | -     |     14.231 (r) | SLOW    |      4.589 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_a[3]     | OSERDESE2 (IO) | -     |     14.231 (r) | SLOW    |      4.590 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_a[4]     | OSERDESE2 (IO) | -     |     14.227 (r) | SLOW    |      4.584 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_a[5]     | OSERDESE2 (IO) | -     |     14.221 (r) | SLOW    |      4.586 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_a[6]     | OSERDESE2 (IO) | -     |     14.235 (r) | SLOW    |      4.592 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_a[7]     | OSERDESE2 (IO) | -     |     14.237 (r) | SLOW    |      4.593 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_a[8]     | OSERDESE2 (IO) | -     |     14.227 (r) | SLOW    |      4.584 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_a[9]     | OSERDESE2 (IO) | -     |     14.220 (r) | SLOW    |      4.585 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_a[10]    | OSERDESE2 (IO) | -     |     14.221 (r) | SLOW    |      4.585 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_a[11]    | OSERDESE2 (IO) | -     |     14.214 (r) | SLOW    |      4.572 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_a[12]    | OSERDESE2 (IO) | -     |     14.226 (r) | SLOW    |      4.585 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_ba[0]    | OSERDESE2 (IO) | -     |     14.225 (r) | SLOW    |      4.588 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_ba[1]    | OSERDESE2 (IO) | -     |     14.217 (r) | SLOW    |      4.581 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_ba[2]    | OSERDESE2 (IO) | -     |     14.229 (r) | SLOW    |      4.589 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_cas_n    | OSERDESE2 (IO) | -     |     14.245 (r) | SLOW    |      4.602 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_cke      | OSERDESE2 (IO) | -     |     14.238 (r) | SLOW    |      4.595 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_clk_n    | OSERDESE2 (IO) | -     |     14.308 (r) | SLOW    |      4.565 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_clk_p    | OSERDESE2 (IO) | -     |     14.320 (r) | SLOW    |      4.577 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_cs_n     | OSERDESE2 (IO) | -     |     14.195 (r) | SLOW    |      4.552 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dm[0]    | OSERDESE2 (IO) | -     |     14.259 (r) | SLOW    |      4.616 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dm[1]    | OSERDESE2 (IO) | -     |     14.262 (r) | SLOW    |      4.620 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dq[0]    | OSERDESE2 (IO) | -     |     15.117 (r) | SLOW    |      4.306 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dq[1]    | OSERDESE2 (IO) | -     |     15.115 (r) | SLOW    |      4.305 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dq[2]    | OSERDESE2 (IO) | -     |     15.118 (r) | SLOW    |      4.292 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dq[3]    | OSERDESE2 (IO) | -     |     15.116 (r) | SLOW    |      4.304 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dq[4]    | OSERDESE2 (IO) | -     |     15.115 (r) | SLOW    |      4.311 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dq[5]    | OSERDESE2 (IO) | -     |     15.115 (r) | SLOW    |      4.296 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dq[6]    | OSERDESE2 (IO) | -     |     15.116 (r) | SLOW    |      4.308 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dq[7]    | OSERDESE2 (IO) | -     |     15.115 (r) | SLOW    |      4.287 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dq[8]    | OSERDESE2 (IO) | -     |     15.101 (r) | SLOW    |      4.295 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dq[9]    | OSERDESE2 (IO) | -     |     15.111 (r) | SLOW    |      4.315 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dq[10]   | OSERDESE2 (IO) | -     |     15.104 (r) | SLOW    |      4.306 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dq[11]   | OSERDESE2 (IO) | -     |     15.111 (r) | SLOW    |      4.319 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dq[12]   | OSERDESE2 (IO) | -     |     15.104 (r) | SLOW    |      4.318 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dq[13]   | OSERDESE2 (IO) | -     |     15.101 (r) | SLOW    |      4.290 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dq[14]   | OSERDESE2 (IO) | -     |     15.112 (r) | SLOW    |      4.312 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dq[15]   | OSERDESE2 (IO) | -     |     15.103 (r) | SLOW    |      4.292 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_odt      | OSERDESE2 (IO) | -     |     14.231 (r) | SLOW    |      4.587 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_ras_n    | OSERDESE2 (IO) | -     |     14.216 (r) | SLOW    |      4.577 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_we_n     | OSERDESE2 (IO) | -     |     14.248 (r) | SLOW    |      4.604 (r) | FAST    | soc_crg_clkout1 |
clk100    | ddram_dqs_n[0] | OSERDESE2 (IO) | -     |     16.781 (r) | SLOW    |      5.972 (r) | FAST    | soc_crg_clkout2 |
clk100    | ddram_dqs_n[1] | OSERDESE2 (IO) | -     |     16.774 (r) | SLOW    |      5.970 (r) | FAST    | soc_crg_clkout2 |
clk100    | ddram_dqs_p[0] | OSERDESE2 (IO) | -     |     16.782 (r) | SLOW    |      5.974 (r) | FAST    | soc_crg_clkout2 |
clk100    | ddram_dqs_p[1] | OSERDESE2 (IO) | -     |     16.775 (r) | SLOW    |      5.970 (r) | FAST    | soc_crg_clkout2 |
----------+----------------+----------------+-------+----------------+---------+----------------+---------+-----------------+


Setup between Clocks

-------+-------------+---------------+---------+---------------+---------+---------------+---------+---------------+---------+
Source | Destination |  Src:Rise     | Process |  Src:Rise     | Process |  Src:Fall     | Process |  Src:Fall     | Process |
Clock  | Clock       | Dest:Rise(ns) | Corner  | Dest:Fall(ns) | Corner  | Dest:Rise(ns) | Corner  | Dest:Fall(ns) | Corner  |
-------+-------------+---------------+---------+---------------+---------+---------------+---------+---------------+---------+
clk100 | clk100      |        12.371 | SLOW    |               |         |               |         |               |         |
-------+-------------+---------------+---------+---------------+---------+---------------+---------+---------------+---------+


Setup / Hold times for input bus
Clocked by: clk100
Worst Case Data Window: 7.522 ns
Ideal Clock Offset to Actual Clock: 6.850 ns
-------------------+-------------+---------+--------------+---------+-----------+-----------+---------------+
                   |             | Process |              | Process | Setup     |  Hold     | Source Offset |
Source             |   Setup(ns) | Corner  |     Hold(ns) | Corner  | Slack(ns) | Slack(ns) | to Center(ns) |
-------------------+-------------+---------+--------------+---------+-----------+-----------+---------------+
ddram_dq[0]        |  -3.185 (r) | FAST    |   10.595 (r) | SLOW    |       inf |       inf |             - |
ddram_dq[0]        |  -3.113 (f) | FAST    |   10.595 (f) | SLOW    |       inf |       inf |             - |
ddram_dq[1]        |  -3.184 (r) | FAST    |   10.592 (r) | SLOW    |       inf |       inf |             - |
ddram_dq[1]        |  -3.112 (f) | FAST    |   10.592 (f) | SLOW    |       inf |       inf |             - |
ddram_dq[2]        |  -3.201 (r) | FAST    |   10.611 (r) | SLOW    |       inf |       inf |             - |
ddram_dq[2]        |  -3.129 (f) | FAST    |   10.611 (f) | SLOW    |       inf |       inf |             - |
ddram_dq[3]        |  -3.184 (r) | FAST    |   10.594 (r) | SLOW    |       inf |       inf |             - |
ddram_dq[3]        |  -3.112 (f) | FAST    |   10.594 (f) | SLOW    |       inf |       inf |             - |
ddram_dq[4]        |  -3.178 (r) | FAST    |   10.586 (r) | SLOW    |       inf |       inf |             - |
ddram_dq[4]        |  -3.106 (f) | FAST    |   10.586 (f) | SLOW    |       inf |       inf |             - |
ddram_dq[5]        |  -3.193 (r) | FAST    |   10.601 (r) | SLOW    |       inf |       inf |             - |
ddram_dq[5]        |  -3.121 (f) | FAST    |   10.601 (f) | SLOW    |       inf |       inf |             - |
ddram_dq[6]        |  -3.180 (r) | FAST    |   10.590 (r) | SLOW    |       inf |       inf |             - |
ddram_dq[6]        |  -3.108 (f) | FAST    |   10.590 (f) | SLOW    |       inf |       inf |             - |
ddram_dq[7]        |  -3.202 (r) | FAST    |   10.611 (r) | SLOW    |       inf |       inf |             - |
ddram_dq[7]        |  -3.130 (f) | FAST    |   10.611 (f) | SLOW    |       inf |       inf |             - |
ddram_dq[8]        |  -3.179 (r) | FAST    |   10.581 (r) | SLOW    |       inf |       inf |             - |
ddram_dq[8]        |  -3.107 (f) | FAST    |   10.581 (f) | SLOW    |       inf |       inf |             - |
ddram_dq[9]        |  -3.170 (r) | FAST    |   10.577 (r) | SLOW    |       inf |       inf |             - |
ddram_dq[9]        |  -3.098 (f) | FAST    |   10.577 (f) | SLOW    |       inf |       inf |             - |
ddram_dq[10]       |  -3.172 (r) | FAST    |   10.575 (r) | SLOW    |       inf |       inf |             - |
ddram_dq[10]       |  -3.100 (f) | FAST    |   10.575 (f) | SLOW    |       inf |       inf |             - |
ddram_dq[11]       |  -3.165 (r) | FAST    |   10.572 (r) | SLOW    |       inf |       inf |             - |
ddram_dq[11]       |  -3.093 (f) | FAST    |   10.572 (f) | SLOW    |       inf |       inf |             - |
ddram_dq[12]       |  -3.161 (r) | FAST    |   10.564 (r) | SLOW    |       inf |       inf |             - |
ddram_dq[12]       |  -3.089 (f) | FAST    |   10.564 (f) | SLOW    |       inf |       inf |             - |
ddram_dq[13]       |  -3.184 (r) | FAST    |   10.586 (r) | SLOW    |       inf |       inf |             - |
ddram_dq[13]       |  -3.112 (f) | FAST    |   10.586 (f) | SLOW    |       inf |       inf |             - |
ddram_dq[14]       |  -3.172 (r) | FAST    |   10.580 (r) | SLOW    |       inf |       inf |             - |
ddram_dq[14]       |  -3.100 (f) | FAST    |   10.580 (f) | SLOW    |       inf |       inf |             - |
ddram_dq[15]       |  -3.185 (r) | FAST    |   10.588 (r) | SLOW    |       inf |       inf |             - |
ddram_dq[15]       |  -3.113 (f) | FAST    |   10.588 (f) | SLOW    |       inf |       inf |             - |
-------------------+-------------+---------+--------------+---------+-----------+-----------+---------------+
Worst Case Summary |  -3.089 (f) | FAST    |   10.611 (r) | SLOW    |       inf |       inf |             - |
-------------------+-------------+---------+--------------+---------+-----------+-----------+---------------+



Max / Min delays for output bus
Clocked by: clk100
Bus Skew: 0.032 ns
-------------------+--------------+---------+-------------+---------+----------+
                   |      Max     | Process |     Min     | Process | Edge     |
Pad                |    Delay(ns) | Corner  |   Delay(ns) | Corner  | Skew(ns) |
-------------------+--------------+---------+-------------+---------+----------+
ddram_a[0]         |   14.204 (r) | SLOW    |   4.566 (r) | FAST    |    0.000 |
ddram_a[1]         |   14.219 (r) | SLOW    |   4.583 (r) | FAST    |    0.017 |
ddram_a[2]         |   14.231 (r) | SLOW    |   4.589 (r) | FAST    |    0.026 |
ddram_a[3]         |   14.231 (r) | SLOW    |   4.590 (r) | FAST    |    0.026 |
ddram_a[4]         |   14.227 (r) | SLOW    |   4.584 (r) | FAST    |    0.022 |
ddram_a[5]         |   14.221 (r) | SLOW    |   4.586 (r) | FAST    |    0.020 |
ddram_a[6]         |   14.235 (r) | SLOW    |   4.592 (r) | FAST    |    0.031 |
ddram_a[7]         |   14.237 (r) | SLOW    |   4.593 (r) | FAST    |    0.032 |
ddram_a[8]         |   14.227 (r) | SLOW    |   4.584 (r) | FAST    |    0.022 |
ddram_a[9]         |   14.220 (r) | SLOW    |   4.585 (r) | FAST    |    0.019 |
ddram_a[10]        |   14.221 (r) | SLOW    |   4.585 (r) | FAST    |    0.020 |
ddram_a[11]        |   14.214 (r) | SLOW    |   4.572 (r) | FAST    |    0.010 |
ddram_a[12]        |   14.226 (r) | SLOW    |   4.585 (r) | FAST    |    0.022 |
-------------------+--------------+---------+-------------+---------+----------+
Worst Case Summary |   14.237 (r) | SLOW    |   4.566 (r) | FAST    |    0.032 |
-------------------+--------------+---------+-------------+---------+----------+



Max / Min delays for output bus
Clocked by: clk100
Bus Skew: 0.012 ns
-------------------+--------------+---------+-------------+---------+----------+
                   |      Max     | Process |     Min     | Process | Edge     |
Pad                |    Delay(ns) | Corner  |   Delay(ns) | Corner  | Skew(ns) |
-------------------+--------------+---------+-------------+---------+----------+
ddram_ba[0]        |   14.225 (r) | SLOW    |   4.588 (r) | FAST    |    0.008 |
ddram_ba[1]        |   14.217 (r) | SLOW    |   4.581 (r) | FAST    |    0.000 |
ddram_ba[2]        |   14.229 (r) | SLOW    |   4.589 (r) | FAST    |    0.012 |
-------------------+--------------+---------+-------------+---------+----------+
Worst Case Summary |   14.229 (r) | SLOW    |   4.581 (r) | FAST    |    0.012 |
-------------------+--------------+---------+-------------+---------+----------+



Max / Min delays for output bus
Clocked by: clk100
Bus Skew: 0.004 ns
-------------------+--------------+---------+-------------+---------+----------+
                   |      Max     | Process |     Min     | Process | Edge     |
Pad                |    Delay(ns) | Corner  |   Delay(ns) | Corner  | Skew(ns) |
-------------------+--------------+---------+-------------+---------+----------+
ddram_dm[0]        |   14.259 (r) | SLOW    |   4.616 (r) | FAST    |    0.000 |
ddram_dm[1]        |   14.262 (r) | SLOW    |   4.620 (r) | FAST    |    0.004 |
-------------------+--------------+---------+-------------+---------+----------+
Worst Case Summary |   14.262 (r) | SLOW    |   4.616 (r) | FAST    |    0.004 |
-------------------+--------------+---------+-------------+---------+----------+



Max / Min delays for output bus
Clocked by: clk100
Bus Skew: 1.968 ns
-------------------+--------------+---------+-------------+---------+----------+
                   |      Max     | Process |     Min     | Process | Edge     |
Pad                |    Delay(ns) | Corner  |   Delay(ns) | Corner  | Skew(ns) |
-------------------+--------------+---------+-------------+---------+----------+
ddram_dq[0]        |   18.737 (r) | SLOW    |   4.306 (r) | FAST    |    1.828 |
ddram_dq[1]        |   18.272 (r) | SLOW    |   4.305 (r) | FAST    |    1.363 |
ddram_dq[2]        |   18.877 (r) | SLOW    |   4.292 (r) | FAST    |    1.968 |
ddram_dq[3]        |   18.713 (r) | SLOW    |   4.304 (r) | FAST    |    1.805 |
ddram_dq[4]        |   18.122 (r) | SLOW    |   4.311 (r) | FAST    |    1.213 |
ddram_dq[5]        |   18.112 (r) | SLOW    |   4.296 (r) | FAST    |    1.203 |
ddram_dq[6]        |   18.573 (r) | SLOW    |   4.308 (r) | FAST    |    1.665 |
ddram_dq[7]        |   17.972 (r) | SLOW    |   4.287 (r) | FAST    |    1.063 |
ddram_dq[8]        |   17.515 (r) | SLOW    |   4.295 (r) | FAST    |    0.607 |
ddram_dq[9]        |   17.213 (r) | SLOW    |   4.315 (r) | FAST    |    0.305 |
ddram_dq[10]       |   16.920 (r) | SLOW    |   4.306 (r) | FAST    |    0.020 |
ddram_dq[11]       |   17.363 (r) | SLOW    |   4.319 (r) | FAST    |    0.455 |
ddram_dq[12]       |   16.909 (r) | SLOW    |   4.318 (r) | FAST    |    0.031 |
ddram_dq[13]       |   17.375 (r) | SLOW    |   4.290 (r) | FAST    |    0.467 |
ddram_dq[14]       |   17.503 (r) | SLOW    |   4.312 (r) | FAST    |    0.595 |
ddram_dq[15]       |   17.213 (r) | SLOW    |   4.292 (r) | FAST    |    0.304 |
-------------------+--------------+---------+-------------+---------+----------+
Worst Case Summary |   18.877 (r) | SLOW    |   4.287 (r) | FAST    |    1.968 |
-------------------+--------------+---------+-------------+---------+----------+



Max / Min delays for output bus
Clocked by: clk100
Bus Skew: 0.847 ns
-------------------+--------------+---------+-------------+---------+----------+
                   |      Max     | Process |     Min     | Process | Edge     |
Pad                |    Delay(ns) | Corner  |   Delay(ns) | Corner  | Skew(ns) |
-------------------+--------------+---------+-------------+---------+----------+
ddram_dqs_n[0]     |   18.034 (r) | SLOW    |   5.470 (r) | FAST    |    0.846 |
ddram_dqs_n[1]     |   17.188 (r) | SLOW    |   5.097 (r) | FAST    |    0.000 |
ddram_dqs_p[0]     |   18.035 (r) | SLOW    |   5.472 (r) | FAST    |    0.847 |
ddram_dqs_p[1]     |   17.189 (r) | SLOW    |   5.097 (r) | FAST    |    0.001 |
-------------------+--------------+---------+-------------+---------+----------+
Worst Case Summary |   18.035 (r) | SLOW    |   5.097 (r) | FAST    |    0.847 |
-------------------+--------------+---------+-------------+---------+----------+




