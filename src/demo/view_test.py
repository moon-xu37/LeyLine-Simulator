from core.simulation import *
from core.entities.character import *
from core.visualize.log_view import LogPrinter
from core.visualize.genshin_color import ColorManager
from core.visualize.sim_view import SimPrinter


if __name__ == '__main__':
    '''
    # TODO 测试文件待删除

    测试逻辑的入口
    '''
    print('START A SIMPLE SIMULATION!')
    simulation = Simulation()
    simulation.set_show_what('numeric', 'buff', 'element', 'warning', 'reject')
    simulation.set_energy_options(tolerance=40, full=True)
    simulation.set_enemy(lv=72)

    simulation.set_character('Shogun', lv=90)
    simulation.set_talents('Shogun', norm=6, skill=9, burst=10, cx=2)

    w = Weapon()
    w.initialize('Engulfing_Lightning', lv=90, asc=False, refine=1)
    simulation.set_weapon('Shogun', w)

    arts = Artifact()
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
    arts.equip(p1, p2, p3, p4, p5)
    simulation.set_artifact('Shogun', arts)

    cmd_list = [
        '1.A@1',
        '1.A@2',
        '1.A@3',
        '1.A@4',
        '1.A@5',
        '1.Q@6',
        '1.A@8',
        '1.Z@9',
        '1.J@10',
        '1.E@11',
        '1.A@12'
    ]
    list(map(lambda s: simulation.insert(Operation(s)),
             cmd_list))
    simulation.start(20)

    numeric_controller = NumericController()
    stage = numeric_controller.onstage_record()

    p = LogPrinter(numeric_controller)
    p.print_char_log('Shogun', ['ER', 'ELECTRO_DMG'])
    p.print_energy_log()
    p.print_damage_log(['Shogun'])

    cm = ColorManager(simulation)
    # cm.test(cm.get_element_color('cryo'))
    # cm.showall()
    
    sp = SimPrinter(simulation)
    sp.print_action(['Shogun'], stage)
    sp.print_buffs(stage)
    sp.print_element()