from core.simulation import *
from core.entities.character import *
from core.visualize.log_view import LogPrinter
from core.visualize.sim_view import SimPrinter
from core.visualize.exporter import Exporter


if __name__ == '__main__':
    '''
    # TODO 测试文件待删除

    测试逻辑的入口
    '''
    print('START A SIMPLE SIMULATION!')
    simulation = Simulation()
    simulation.set_show_what('warning', 'reject', 'element')
    simulation.set_energy_options(tolerance=40, full=True)
    simulation.set_enemy(lv=90)

    simulation.set_character('Shogun', lv=90)
    simulation.set_talents('Shogun', norm=6, skill=9, burst=10, cx=2)

    simulation.set_character('Albedo', lv=80, asc=True)
    simulation.set_talents('Albedo', norm=6, skill=9, burst=10, cx=2)

    simulation.set_character('Hutao', lv=90)
    simulation.set_talents('Hutao', norm=10, skill=10, burst=10, cx=2)

    w1 = Weapon()
    w1.initialize('Engulfing_Lightning', lv=90, asc=False, refine=5)
    simulation.set_weapon('Shogun', w1)

    w2 = Weapon()
    w2.base.initialize(name='Festering_Desire', lv=90, asc=False, refine=5)
    simulation.set_weapon('Albedo', w2)

    w3 = Weapon()
    w3.initialize('Engulfing_Lightning', lv=90, asc=False, refine=5)
    simulation.set_weapon('Hutao', w3)

    art1 = Artifact()
    p1 = ArtifactPiece(
        'JUE_YUAN@FLOWER@[HP_CONST]@[ER:17,CRIT_RATE:27,CRIT_DMG:15,ATK_PER:8,]@LV20@STAR5;')
    p2 = ArtifactPiece(
        'JUE_YUAN@PLUME@[ATK_CONST]@[CRIT_DMG:17,CRIT_RATE:18,ATK_PER:23,DEF_PER:10,]@LV20@STAR5;')
    p3 = ArtifactPiece(
        'JUE_DOU_SHI@SANDS@[ER]@[CRIT_DMG:17,ATK_CONST:8,DEF_PER:24,CRIT_RATE:27,]@LV20@STAR5;')
    p4 = ArtifactPiece(
        'JUE_YUAN@GOBLET@[ATK_PER]@[ATK_CONST:8,CRIT_DMG:16,ER:14,CRIT_RATE:22,]@LV20@STAR5;')
    p5 = ArtifactPiece(
        'JUE_YUAN@CIRCLET@[CRIT_RATE]@[CRIT_DMG:18,ER:9,ATK_PER:25,EM:15,]@LV20@STAR5;')
    art1.equip(p1, p2, p3, p4, p5)
    simulation.set_artifact('Shogun', art1)

    art2 = Artifact()
    p1_ = ArtifactPiece(
        'ZONG_SHI@FLOWER@[HP_CONST]@[ATK_PER:23,CRIT_DMG:27,EM:15,ER:7,]@LV20@STAR5;')
    p2_ = ArtifactPiece(
        'ZONG_SHI@PLUME@[ATK_CONST]@[HP_PER:8,CRIT_RATE:27,CRIT_DMG:26,HP_CONST:16,]@LV20@STAR5;')
    p3_ = ArtifactPiece(
        'ZONG_SHI@SANDS@[DEF_PER]@[DEF_CONST:9,CRIT_DMG:32,CRIT_RATE:16,ER:15,]@LV20@STAR5;')
    p4_ = ArtifactPiece(
        'ZHUI_YI@GOBLET@[GEO_DMG]@[HP_CONST:36,HP_PER:9,CRIT_RATE:29,ATK_PER:10,]@LV20@STAR5;')
    p5_ = ArtifactPiece(
        'ZONG_SHI@CIRCLET@[CRIT_RATE]@[DEF_CONST:26,ATK_CONST:8,CRIT_DMG:26,ATK_PER:17,]@LV20@STAR5;')
    art2.equip(p1_, p2_, p3_, p4_, p5_)
    simulation.set_artifact('Albedo', art2)

    art3 = Artifact()
    art3.equip(p1, p2, p3, p4, p5)
    simulation.set_artifact('Hutao', art3)

    cmds = \
        '''
        1.e@0
        2.c@1
        2.e@2
        3.c@3
        3.e@3.5
        3.a@4
        3.z@4.5
        3.a@5.5
        3.z@6
        3.q@7.5
        2.c@10
        2.q@11
        1.c@15
        1.q@16
        1.a@18
        1.z@18.5
        1.a@20
        1.z@20.5
        3.c@22
        3.e@25
        3.q@26
        '''
    cmd_list = [c.strip() for c in cmds.split()]
    list(map(lambda s: simulation.insert(Operation(s)),
             cmd_list))
    import time
    t1 = time.perf_counter()
    simulation.start()
    t2 = time.perf_counter()
    print('freq={:.1f}'.format(1/(t2-t1)))

    numeric_controller = NumericController()
    stage = numeric_controller.onstage_record()

    p = LogPrinter(numeric_controller)
    p.paint_color(simulation)
    # p.print_char_log('Shogun', ['ATK', 'ER', 'ELECTRO_DMG', 'EM'])
    # p.print_char_log('Albedo', ['ATK', 'DEF', 'CRIT_RATE'])
    # p.print_char_log('Hutao', ['ATK'])
    # p.print_energy_log()
    # p.print_damage_one('Shogun')
    # p.print_damage_one('Albedo')
    # p.print_damage_one('Hutao')
    # p.print_heal_one('Hutao')
    # p.print_damage_pie()
    # p.print_element_log()
    p.print_damage_stackbar(interval=2)
    p.print_damage_stack()

    sp = SimPrinter(simulation)
    # sp.print_action(['Shogun', 'Albedo', 'Hutao'], stage)
    # sp.print_buffs(stage)
    # sp.print_element()
    # sp.print_energy(stage)
    
    e = Exporter(simulation)
    e.export_dir(r'./')
    # e.export()
