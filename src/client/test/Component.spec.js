import { mount, shallowMount } from '@vue/test-utils'
import TheDrawer from '@/components/app/TheDrawer.vue'

const factory = () => {
  return shallowMount(TheDrawer, {})
}

describe('TheDrawer', () => {
  test('is a Vue instance', () => {
    const wrapper = mount(TheDrawer)
    expect(wrapper.isVueInstance()).toBeTruthy()
  })

  test('renders properly', () => {
    const wrapper = factory()
    expect(wrapper.html()).toMatchSnapshot()
  })
})
