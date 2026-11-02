Copyright 1986-2022 Xilinx, Inc. All Rights Reserved. Copyright 2022-2024 Advanced Micro Devices, Inc. All Rights Reserved.
---------------------------------------------------------------------------------------------------------------------------------------------
| Tool Version : Vivado v.2024.1 (lin64) Build 5076996 Wed May 22 18:36:09 MDT 2024
| Date         : Wed Oct  7 10:01:19 2026
| Host         : LAPTOP-CSM08B9Q running 64-bit Ubuntu 26.04 LTS
| Command      : report_utilization -hierarchical -file digilent_nexys4ddr_utilization_hierarchical_place.rpt
| Design       : digilent_nexys4ddr
| Device       : xc7a100tcsg324-1
| Speed File   : -1
| Design State : Fully Placed
---------------------------------------------------------------------------------------------------------------------------------------------

Utilization Design Information

Table of Contents
-----------------
1. Utilization by Hierarchy

1. Utilization by Hierarchy
---------------------------

+-----------------------------------+-----------------------------+------------+------------+---------+------+------+--------+--------+------------+
|              Instance             |            Module           | Total LUTs | Logic LUTs | LUTRAMs | SRLs |  FFs | RAMB36 | RAMB18 | DSP Blocks |
+-----------------------------------+-----------------------------+------------+------------+---------+------+------+--------+--------+------------+
| digilent_nexys4ddr                |                       (top) |       6187 |       6040 |     144 |    3 | 4504 |     15 |     33 |          8 |
|   (digilent_nexys4ddr)            |                       (top) |       1668 |       1522 |     144 |    2 | 1958 |     10 |     17 |          0 |
|   Cfu                             |                         Cfu |       1511 |       1510 |       0 |    1 | 1081 |      4 |      8 |          4 |
|     (Cfu)                         |                         Cfu |         30 |         30 |       0 |    0 |   37 |      0 |      0 |          0 |
|     fn0                           |                         fn0 |       1481 |       1480 |       0 |    1 | 1044 |      4 |      8 |          4 |
|       (fn0)                       |                         fn0 |          2 |          2 |       0 |    0 |    0 |      0 |      0 |          0 |
|       FIFO                        |                        FIFO |         34 |         34 |       0 |    0 |   28 |      0 |      1 |          0 |
|         (FIFO)                    |                        FIFO |          0 |          0 |       0 |    0 |    1 |      0 |      0 |          0 |
|         unbuffered                |                  unbuffered |         34 |         34 |       0 |    0 |   27 |      0 |      1 |          0 |
|       acc                         |                         acc |        130 |        130 |       0 |    0 |   32 |      0 |      0 |          0 |
|       btw                         |                         btw |         16 |         16 |       0 |    0 |   32 |      0 |      0 |          0 |
|       f7buf                       |                       f7buf |          0 |          0 |       0 |    0 |    7 |      0 |      0 |          0 |
|       fvf                         |                         fvf |        171 |        171 |       0 |    0 |  172 |      0 |      0 |          0 |
|         (fvf)                     |                         fvf |          2 |          2 |       0 |    0 |    3 |      0 |      0 |          0 |
|         smr_0                     |                       smr_0 |        115 |        115 |       0 |    0 |   43 |      0 |      0 |          0 |
|         smr_1                     |                       smr_1 |         18 |         18 |       0 |    0 |   42 |      0 |      0 |          0 |
|         smr_2                     |                       smr_2 |         18 |         18 |       0 |    0 |   42 |      0 |      0 |          0 |
|         smr_3                     |                       smr_3 |         19 |         19 |       0 |    0 |   42 |      0 |      0 |          0 |
|       ins                         |                         ins |        248 |        248 |       0 |    0 |  197 |      4 |      0 |          0 |
|         (ins)                     |                         ins |         25 |         25 |       0 |    0 |   28 |      0 |      0 |          0 |
|         dp_0                      |                        dp_0 |          1 |          1 |       0 |    0 |    0 |      1 |      0 |          0 |
|         dp_1                      |                        dp_1 |          2 |          2 |       0 |    0 |    0 |      1 |      0 |          0 |
|         dp_2                      |                        dp_2 |          1 |          1 |       0 |    0 |    0 |      1 |      0 |          0 |
|         dp_3                      |                        dp_3 |          2 |          2 |       0 |    0 |    0 |      1 |      0 |          0 |
|         smr_0                     |                     smr_0$1 |        141 |        141 |       0 |    0 |   43 |      0 |      0 |          0 |
|         smr_1                     |                     smr_1$2 |         14 |         14 |       0 |    0 |   42 |      0 |      0 |          0 |
|         smr_2                     |                     smr_2$3 |         50 |         50 |       0 |    0 |   42 |      0 |      0 |          0 |
|         smr_3                     |                     smr_3$4 |         16 |         16 |       0 |    0 |   42 |      0 |      0 |          0 |
|       ins_set                     |                     ins_set |          0 |          0 |       0 |    0 |    1 |      0 |      0 |          0 |
|       madd                        |                        madd |        318 |        318 |       0 |    0 |   87 |      0 |      0 |          0 |
|       mark_read                   |                   mark_read |          1 |          1 |       0 |    0 |   33 |      0 |      0 |          0 |
|       oq_get                      |                      oq_get |          0 |          0 |       0 |    0 |    1 |      0 |      0 |          0 |
|       pp                          |                          pp |        247 |        247 |       0 |    0 |   97 |      0 |      0 |          4 |
|         (pp)                      |                          pp |         80 |         80 |       0 |    0 |   47 |      0 |      0 |          0 |
|         srdhm                     |                       srdhm |        167 |        167 |       0 |    0 |   50 |      0 |      0 |          4 |
|       seq                         |                         seq |         55 |         54 |       0 |    1 |   31 |      0 |      0 |          0 |
|         f_count                   |                     f_count |          7 |          7 |       0 |    0 |   12 |      0 |      0 |          0 |
|         four_count                |                  four_count |          4 |          4 |       0 |    0 |    3 |      0 |      0 |          0 |
|         gate_calc                 |                   gate_calc |          0 |          0 |       0 |    0 |    1 |      0 |      0 |          0 |
|         i_count                   |                     i_count |          9 |          9 |       0 |    0 |   11 |      0 |      0 |          0 |
|         madd_delay                |                  madd_delay |         33 |         33 |       0 |    0 |    2 |      0 |      0 |          0 |
|         pp_delay                  |                    pp_delay |          2 |          1 |       0 |    1 |    2 |      0 |      0 |          0 |
|       set_activation_max          |          set_activation_max |          0 |          0 |       0 |    0 |   32 |      0 |      0 |          0 |
|       set_activation_min          |          set_activation_min |         24 |         24 |       0 |    0 |   32 |      0 |      0 |          0 |
|       set_input_depth_words       |       set_input_depth_words |         70 |         70 |       0 |    0 |   33 |      0 |      0 |          0 |
|       set_input_offset            |            set_input_offset |          5 |          5 |       0 |    0 |   32 |      0 |      0 |          0 |
|       set_output_batch_size       |       set_output_batch_size |          3 |          3 |       0 |    0 |   34 |      0 |      0 |          0 |
|       set_output_depth            |            set_output_depth |          0 |          0 |       0 |    0 |   32 |      0 |      0 |          0 |
|       set_output_offset           |           set_output_offset |          0 |          0 |       0 |    0 |   32 |      0 |      0 |          0 |
|       start_run                   |                   start_run |          2 |          2 |       0 |    0 |   33 |      0 |      0 |          0 |
|       store_filter_values_dp_0    |    store_filter_values_dp_0 |          0 |          0 |       0 |    0 |    0 |      0 |      1 |          0 |
|       store_filter_values_dp_1    |    store_filter_values_dp_1 |          0 |          0 |       0 |    0 |    0 |      0 |      1 |          0 |
|       store_filter_values_dp_2    |    store_filter_values_dp_2 |          0 |          0 |       0 |    0 |    0 |      0 |      1 |          0 |
|       store_filter_values_dp_3    |    store_filter_values_dp_3 |          0 |          0 |       0 |    0 |    0 |      0 |      1 |          0 |
|       store_filter_values_set     |     store_filter_values_set |         44 |         44 |       0 |    0 |   12 |      0 |      0 |          0 |
|       store_output_bias_dp        |        store_output_bias_dp |          0 |          0 |       0 |    0 |    0 |      0 |      1 |          0 |
|       store_output_bias_inc       |       store_output_bias_inc |         12 |         12 |       0 |    0 |    9 |      0 |      0 |          0 |
|       store_output_bias_set       |       store_output_bias_set |         15 |         15 |       0 |    0 |    9 |      0 |      0 |          0 |
|       store_output_multiplier_dp  |  store_output_multiplier_dp |          0 |          0 |       0 |    0 |    0 |      0 |      1 |          0 |
|       store_output_multiplier_inc | store_output_multiplier_inc |         12 |         12 |       0 |    0 |    9 |      0 |      0 |          0 |
|       store_output_multiplier_set | store_output_multiplier_set |         15 |         15 |       0 |    0 |    9 |      0 |      0 |          0 |
|       store_output_shift_dp       |       store_output_shift_dp |         41 |         41 |       0 |    0 |    0 |      0 |      1 |          0 |
|       store_output_shift_inc      |      store_output_shift_inc |         12 |         12 |       0 |    0 |    9 |      0 |      0 |          0 |
|       store_output_shift_set      |      store_output_shift_set |         15 |         15 |       0 |    0 |    9 |      0 |      0 |          0 |
|   VexRiscv                        |                    VexRiscv |       3012 |       3012 |       0 |    0 | 1465 |      1 |      8 |          4 |
|     (VexRiscv)                    |                    VexRiscv |       1620 |       1620 |       0 |    0 | 1311 |      0 |      2 |          4 |
|     IBusCachedPlugin_cache        |            InstructionCache |        816 |        816 |       0 |    0 |   95 |      1 |      1 |          0 |
|     dataCache_1                   |                   DataCache |        585 |        585 |       0 |    0 |   59 |      0 |      5 |          0 |
+-----------------------------------+-----------------------------+------------+------------+---------+------+------+--------+--------+------------+
* Note: The sum of lower-level cells may be larger than their parent cells total, due to cross-hierarchy LUT combining


