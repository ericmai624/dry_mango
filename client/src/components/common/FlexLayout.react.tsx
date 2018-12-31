import * as React from 'react';
import styled from 'styled-components';

type Align = 'center' | 'end' | 'start';
type Justify = 'all' | 'center' | 'end' | 'even' | 'start';
type Direction = 'horizontal' | 'vertical';
type DefaultProps = Readonly<typeof defaultProps>;
type Props = {
  children: React.ReactChild;
} & Partial<DefaultProps>;

const defaultProps = {
  align: 'start' as Align,
  direction: 'horizontal' as Direction,
  justify: 'start' as Justify,
};

const mapAlign = {
  center: 'center',
  end: 'end',
  start: 'start',
};

const mapDirection = {
  horizontal: 'row',
  vertical: 'column',
};

const mapJustify = {
  all: 'space-between',
  center: 'center',
  end: 'flex-end',
  even: 'space-around',
  start: 'flex-start',
};

const Flex = styled.div<Props>`
  align-items: ${({ align }) => mapAlign[align]};
  flex-direction: ${({ direction }) => mapDirection[direction]};
  justify-content: ${({ justify }) => mapJustify[justify]};
  width: 100%;
`;

function FlexLayout({ children, ...rest }: Props): JSX.Element {
  return <Flex {...rest}>{children}</Flex>;
}

FlexLayout.defaultProps = defaultProps;

export default FlexLayout;
